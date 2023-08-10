# GOMOKU GAME
#----------------------------------

EMPTY = "|"
PLAYER_X = "X"
PLAYER_O = "O"

class Gomoku:
    def __init__(self, size=15):
        self.size = size
        self.board = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.current_player = PLAYER_X

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def make_move(self, row, col):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            r, c = row, col
            while count < 5:
                r += dr
                c += dc
                if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            r, c = row, col
            while count < 5:
                r -= dr
                c -= dc
                if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

    def switch_player(self):
        self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O

    def play(self):
        print("Welcome to Gomoku!")
        print("Players take turns to make a move. The first player to get five in a row wins.")
        print("Enter row and column numbers (both starting from 0) to make a move.")
        print("Have fun!\n")

        while True:
            self.print_board()
            row = int(input(f"Player {self.current_player}, enter row: "))
            col = int(input(f"Player {self.current_player}, enter column: "))

            if 0 <= row < self.size and 0 <= col < self.size:
                if self.make_move(row, col):
                    if self.check_winner(row, col):
                        self.print_board()
                        print(f"Congratulations! Player {self.current_player} wins!")
                        break
                    self.switch_player()
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid row or column. Try again.")

if __name__ == "__main__":
    game = Gomoku()
    game.play()
