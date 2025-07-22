# board.py
class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def display(self):
        print("\n")
        for i in range(3):
            print(" " + " | ".join(self.cells[i * 3 : (i + 1) * 3]))
            if i < 2:
                print("---|---|---")
        print("\n")

    def update(self, position, player):
        if self.cells[position] == " ":
            self.cells[position] = player
            return True
        return False

    def is_full(self):
        return " " not in self.cells

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # columns
            [0, 4, 8],
            [2, 4, 6],  # diagonals
        ]
        for combo in win_conditions:
            if all(self.cells[i] == player for i in combo):
                return True
        return False
