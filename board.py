from settings import Settings


class Board:
    """Class to solve the given sudoku board"""
    def __init__(self):
        self.brd = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        self.settings = Settings

    def print_board(self) -> None:
        for i in range(len(self.brd)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(self.brd[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.brd[i][j])
                else:
                    print(str(self.brd[i][j]) + " ", end="")

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(i, (row, col)):
                self.brd[row][col] = i

                if self.solve():
                    return True

                self.brd[row][col] = 0

        return False

    def valid(self, num, pos):
        # Check row
        for i in range(len(self.brd[0])):
            if self.brd[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(self.brd)):
            if self.brd[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.brd[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self):
        for i in range(len(self.brd)):
            for j in range(len(self.brd[0])):
                if self.brd[i][j] == 0:
                    return i, j  # row, col
        return None


if __name__ == '__main__':
    b1 = Board()
    b1.print_board()
    b1.solve()
    print("\n\n___________________\n\n")
    b1.print_board()
