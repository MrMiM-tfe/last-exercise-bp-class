from textual.app import App
from textual import on
from textual.widgets import Log, Input
import socketio

sio = socketio.Client()

name = input("Enter your name: ")
sio.connect('http://localhost:3000', auth={'name': name})

init_message = f"""
States:
    name: {name}
Select:
    1: createRoom
    2: joinRoom
"""

class WelcomeApp(App):
    options = ["1", "2"]
    current_message = init_message
    msg_grp = 1

    inputMode = 'cmd'

    room = None
    owner = False
    canPlay = False
    ready = False
    playing = False

    def compose(self):
        yield Log(id="cmds", highlight= True)
        yield Log(id="messages")
        yield Input(placeholder="command", id="cmd")

    def on_ready(self):
        self.messages = self.query_one("#messages", Log)
        self.cmds = self.query_one("#cmds", Log)
        
        self.cmds.write(self.current_message)

        self.myInput = self.query_one("#cmd", Input)
        self.myInput.focus()

    @on(Input.Submitted, "#cmd")
    def Submitted(self, i):
        value = i.value
        self.myInput.value = ""

        if len(value) > 2 and value[0] == "/":
            sio.emit("sendMessage", {"content": value[1:], "roomId": self.room})
            return

        if (self.inputMode == 'cmd'):
            cmd = value

            if cmd not in self.options:
                self.cmds.clear()
                self._update_cmds(self.current_message + "\n [Error] invalid command.")
            else:
                self._update_cmds(self.current_message)

            if self.msg_grp == 1:
                if cmd == "1":
                    self._createRoom()
                elif cmd == "2":
                    self._switch_input_mode("roomId")
            elif self.msg_grp == 2 or self.msg_grp == 3:
                if cmd == "1":
                    self.ready = sio.call("setReady", {"ready": not self.ready, "roomId": self.room})
                    self._updateMessage()
                elif cmd == "2":
                    msg = sio.call("playNewRound", {"roomId": self.room})
                    self._update_cmds(self.current_message + f"\n [Message] {msg}")
        elif (self.inputMode == "roomId"):
            self._joinRoom(value)
            self._switch_input_mode("cmd")
        elif (self.inputMode == "play"):
            sio.emit("setUserScore", {"score": value, "roomId": self.room})

    def _switch_input_mode(self, mode):
        self.inputMode = mode
        if (mode == "cmd"):
            self.myInput.placeholder = "command"
        elif mode == "roomId":
            self.myInput.placeholder = "room id"
        elif mode == "play":
            self.myInput.placeholder = "value"

    def _update_cmds(self, string):
        self.cmds.clear()
        self.cmds.write(string)

    def _createRoom(self):
        name = input("Enter room name: ")
        self.room = sio.call("createRoom", {"name": name})
        
        @sio.event
        def playBtnState(data):
            self.canPlay = data["canPlay"]
            self._updateMessage()

        self.owner = True
        self._listen_for_game()
        self._updateMessage()

    def _joinRoom(self, roomId):
        res, msg = sio.call("joinRoom", {"roomId": roomId})
        if (res) :
            self.room = roomId
        self._listen_for_game()
        self._updateMessage()

    def _listen_for_game(self):
        @sio.event
        def newRound(data):
            self.playing = True
            self._updateMessage()

        @sio.event
        def winner(data):
            self._update_cmds(str(data))

        @sio.event
        def newMessage(data):
            self.messages.write_line(data)

        msgs = sio.call("getMessages", {"roomId": self.room})
        for msg in msgs:
            self.messages.write_line(msg)

    def _updateMessage(self):
        if self.owner and not self.playing:
            self.msg_grp = 2
            self.current_message = f"""
                States:
                    name: {name}
                    room: {self.room}
                    ready: {self.ready}
                    owner: {self.owner}
                Select:
                    1: { "UnReady" if self.ready else "Ready" }
                    2: playNewRound {"<Wait for players [u] to check>" if not self.canPlay else ""}
            """
        elif not self.playing:
            self.msg_grp = 3
            self.options = ["1"]
            self.current_message = f"""
                States:
                    name: {name}
                    room: {self.room}
                    ready: {self.ready}
                    owner: {self.owner}
                Select:
                    1: { "UnReady" if self.ready else "Ready" }
            """
        else:
            self.current_message = "type value"
            self._switch_input_mode("play")

        self._update_cmds(self.current_message)


if __name__ == "__main__":
    app = WelcomeApp()
    app.run()