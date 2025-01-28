class TickTackToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.current_player = self.player_1
        self.print_board()
            
    def print_board(self):
        print('  0 1 2')
        print('-' * 7)
        i = 0
        for row in self.board:
            print(i, end='|')
            print('|'.join(row))
            print('-' * 7)
            i += 1

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.print_board()

            if self.check_winner():
                print(f'{self.current_player} wins!')
                self.current_winner = self.current_player
                return "END"
            
            if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
                print("It's a tie!")
                return "END"
            
            self.current_player = self.player_1 if self.current_player == self.player_2 else self.player_2
            return "CONTINUE"
        else:
            print('Invalid move. Try again.')
            return False
        
    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None
        self.current_player = self.player_1
        self.print_board()


game = TickTackToe()

while True:
    while True:
        current_player = game.current_player
        row, col = map(int, input(f"{current_player}: Enter row and column (link this: 0 1): ").split())
        result = game.make_move(row, col)
        if result == "END":
            break
    game.reset_game()