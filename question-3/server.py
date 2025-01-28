import socketio
import eventlet
import uuid

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.ready = False

class Message:
    def __init__(self, user, content):
        self.id = str(uuid.uuid4())
        self.user = user
        self.content = content
    def __str__(self):
        return f"{self.user.name}: {self.content}"

class Room:
    messages = []
    scores: dict[str, int] = {}
    isPlaying = False

    def __init__(self, name, owner):
        self.id = str(uuid.uuid4())
        self.name = name
        self.owner = owner
        self.users: dict[str, User] = {owner.id: owner}

    def addMessage(self, user, content):
        msg = Message(user, content)
        self.messages.append(msg)
        sio.emit("newMessage", str(msg), room=self.id)

    def addUser(self, user):
        if user.id in self.users:
            return (False, "User already in room")
        self.users[user.id] = user
        return (True, "User added to room")

    def canPlayNewRound(self):
        result = len(self.users) >= 2 and all([user.ready for user in self.users.values()]) and not self.isPlaying
        sio.emit("playBtnState", {"canPlay": result}, self.owner.id)
        return result

    def playNewRound(self):
        if not self.canPlayNewRound():
            return (False, "Not enough players")

        self.messages = []
        
        self.scores = {user.id: -1 for user in self.users.values()}
        self.isPlaying = True
        sio.emit("playBtnState", {"canPlay": False}, self.owner.id)
        return (True, "New round started")
    
    def setUserScore(self, user, score):
        if user.id not in self.scores:
            return (False, "User not in room")
        if (self.scores[user.id] > -1):
            return (False, "User already sent a score")
        self.scores[user.id] = score
        print(self.scores)
        if all([score > -1 for score in self.scores.values()]):
            res = self.checkWinner()
            print(res)
        return (True, "Score set")

    def checkWinner(self):
        max_score = max(self.scores.values())
        winners = [user for user, score in self.scores.items() if score == max_score]
        winners = [user.name for user in self.users.values() if user.id in winners]
        sio.emit("winner", {"winners": winners}, room=self.id)
        self.isPlaying = False
        for user in self.users:
            self.users[user].ready = False
        return (True, "Winner(s) found")

class Server:
    users: dict[str, User] = {}
    rooms: dict[str, Room] = {}

    def __init__(self):
        self._register_events()

    def _register_events(self):
        @sio.event
        def connect(sid, environ, auth):
            print("connected", sid)
            user = User(sid, auth["name"])
            self.users[sid] = user
        
        @sio.event
        def disconnect(sid):
            print("disconnected", sid)
            self.users.pop(sid)

        @sio.event
        def createRoom(sid, data):
            # check user
            if (sid not in self.users):
                return

            # create room
            room = Room(data["name"], self.users[sid])
            self.rooms[room.id] = room

            print("room created", room.name)

            sio.enter_room(sid, room.id)
            return room.id
        
        @sio.event
        def setReady(sid, data):
            # check user
            if (sid not in self.users):
                return
            
            # check room
            if (data["roomId"] not in self.rooms):
                return

            self.users[sid].ready = data["ready"]

            room = self.rooms[data["roomId"]]
            room.canPlayNewRound()

            return self.users[sid].ready

        @sio.event
        def joinRoom(sid, data):
            # check user
            if (sid not in self.users):
                return

            # check room
            if (data["roomId"] not in self.rooms):
                return
            
            room = self.rooms[data["roomId"]]
            sio.enter_room(sid, room.id)
            return room.addUser(self.users[sid])
        
        @sio.event
        def setUserScore(sid, data):
            # check user
            if (sid not in self.users):
                return

            # check room
            if (data["roomId"] not in self.rooms):
                return

            room = self.rooms[data["roomId"]]
            
            return room.setUserScore(self.users[sid], int(data["score"]))

        @sio.event
        def playNewRound(sid, data):
            # check user
            if (sid not in self.users):
                return
            
            # check room
            if (data["roomId"] not in self.rooms):
                return
            
            room = self.rooms[data["roomId"]]
            # check room owner
            if (room.owner.id != sid):
                return

            # play new round
            result, msg = room.playNewRound()
            if not result:
                return msg
            
            # send message to all users in room
            sio.emit("newRound", {"roomId": room.id, "msg": msg}, room=room.id)

        @sio.event
        def sendMessage(sid, data):
            # check user
            if (sid not in self.users):
                return
            
            # check room
            if (data["roomId"] not in self.rooms):
                return
            
            room = self.rooms[data["roomId"]]
            room.addMessage(self.users[sid], data["content"])

        @sio.event
        def getMessages(sid, data):
            # check user
            if (sid not in self.users):
                return

            # check room
            if (data["roomId"] not in self.rooms):
                return

            room = self.rooms[data["roomId"]]
            messages = [str(msg) for msg in room.messages]
            return messages


Server()

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 3000)), app)