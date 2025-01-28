import random
    
class Room:
    round = 0
    number_of_cards = 5
    players = []
    played_cards = {}
    messages = {}

    def __init__(self, room_name):
        self.room_name = room_name.lower().strip().replace(" ", "_")

    def add_player(self, player):
        if player in self.players:
            return
        player.room = self
        player.in_room_score = 0
        self.players.append(player)

    def remove_player(self, player):    
        if player not in self.players:
            return
        player.room = None
        player.in_room_score = 0
        self.players.remove(player)

    def deal_cards(self):
        self.round = 0
        cards = [i for i in range(1, (len(self.players) * self.number_of_cards) + 1)]
        random.shuffle(cards)
        for player in self.players:
            player.cards = cards[:self.number_of_cards]
            del cards[:self.number_of_cards]


    def _get_winner(self):
        if (set(self.players) == set(self.played_cards.keys())):
            return max(self.played_cards, key=self.played_cards.get)
        
        print("all players haven't played")
        return None
    
    def get_winner(self):
        if self.round > 4:
            print("please deal new cards")
            return None
        
        self.round += 1
        winner = self._get_winner()
        if winner:
            winner.in_room_score += 1
            self.played_cards = {}
            for player in self.players:
                player.cards = []
            return winner
        return None
    
    def get_messages(self):
        return [f"{player.name}: {message}" for player, message in self.messages.items()]


class Player:
    cards = []
    room: Room = None
    in_room_score = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def leave_room(self):
        if self.room:
            self.room.remove_player(self)

    def send_message(self, message):
        if self.room:
            self.room.messages[self] = message

    def play_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            self.room.played_cards[self] = card

class Game:
    def __init__(self):
        self.players = []
        self.rooms =  []
        
    def create_room(self, room_name):
        room = Room(room_name)
        self.rooms.append(room)
        return room
    
    def get_room(self, room_name) -> Room:
        for room in self.rooms:
            if room.room_name == room_name:
                return room
        return None

game = Game()

# Create a room
game.create_room("room1")

room_1 = game.get_room("room1")

# Create players
player1 = Player("Player 1", 1)
player2 = Player("Player 2", 2)
player3 = Player("Player 3", 3)

# Add players to the room
room_1.add_player(player1)
room_1.add_player(player2)
room_1.add_player(player3)

# Leave the room
player3.leave_room()
# or 
room_1.remove_player(player3)

# send messages
player1.send_message("Hello")
player2.send_message("Hi")

# show messages
for msg in room_1.get_messages():
    print(msg)

# deal cards
room_1.deal_cards()

print(player1.cards)
print(player2.cards)


# play cards
player1.play_card(player1.cards[0])
player2.play_card(player2.cards[3])

# get winner
winner = room_1.get_winner()
print(f"winner is {winner.name}")

# get score
print(player1.in_room_score)
print(player2.in_room_score)