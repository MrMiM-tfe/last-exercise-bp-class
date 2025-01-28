# TikTakToe Game

## how to use class
- make a new instance of class
- use method `make_move` to make a move
    - if the move is valid, the game will continue and if not the current player will be asked to make a move again
    - if the game is over, the game will be reset and the current player will be asked to make a move again
    
    
- use method `reset_game` to reset the game
- use method `current_player` to get the current player
```python
game = TickTackToe()

while True:
    while True:
        current_player = game.current_player
        row, col = map(int, input(f"{current_player}: Enter row and column (link this: 0 1): ").split())
        result = game.make_move(row, col)
        if result == "END":
            break
    game.reset_game()
```
### example output
```bash
  0 1 2
-------
0| | |
-------
1| | |
-------
2| | |
-------
X: Enter row and column (link this: 0 1): 0 0
  0 1 2
-------
0|X| |
-------
1| | |
-------
2| | |
-------
O: Enter row and column (link this: 0 1): 1 1
  0 1 2
-------
0|X| |
-------
1| |O|
-------
2| | |
-------
X: Enter row and column (link this: 0 1): 0 1
  0 1 2
-------
0|X|X| 
-------
1| |O| 
-------
2| | |
-------
O: Enter row and column (link this: 0 1):  2 2
  0 1 2
-------
0|X|X|
-------
1| |O|
-------
2| | |O
-------
X: Enter row and column (link this: 0 1): 0 2
  0 1 2
-------
0|X|X|X
-------
1| |O|
-------
2| | |O
-------
X wins!
  0 1 2
-------
0| | |
-------
1| | |
-------
2| | |
-------
X: Enter row and column (link this: 0 1):
```