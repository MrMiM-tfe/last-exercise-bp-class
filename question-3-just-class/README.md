## How to play the game
```py
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
```
output:
```bash
Player 1: Hello
Player 2: Hi
[6, 4, 10, 9, 2]
[1, 8, 5, 7, 3]
winner is Player 2
0
1
```