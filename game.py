# game.py
from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_move(self):
        while True:
            try:
                move = (
                    int(input(f"Player {self.current_player}, enter position (1-9): "))
                    - 1
                )
                if move < 0 or move > 8:
                    raise ValueError("Invalid range")
                if self.board.update(move, self.current_player):
                    break
                else:
                    print("Cell already taken! Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

    def play(self):
        while True:
            self.board.display()
            self.get_move()
            if self.board.check_winner(self.current_player):
                self.board.display()
                print(f"🎉 Player {self.current_player} wins!")
                break
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break
            self.switch_player()
