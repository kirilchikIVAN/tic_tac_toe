from Symbol import Symbol


class Field:
    SIZE = 3
    TO_WIN = 3

    def __init__(self):
        self.field = [
            [Symbol.NONE] * self.SIZE
            for i in range(self.SIZE)
        ]

    def make_move(self, pos, symbol: Symbol):
        if self.field[pos[0]][pos[1]] != Symbol.NONE:
            return 'occupied'
        else:
            self.field[pos[0]][pos[1]] = symbol
            return 'success'

    def check_win(self):
        for i in range(self.SIZE):
            row_sum = sum(self.field[i])
            if abs(row_sum) == self.TO_WIN:
                return True

        for j in range(self.SIZE):
            col_sum = sum([self.field[i][j] for i in range(self.SIZE)])
            if abs(col_sum) == self.TO_WIN:
                return True

        left_cross = abs(sum([self.field[i][i] for i in range(self.SIZE)]))
        if abs(left_cross) == self.TO_WIN:
            return True

        right_cross = abs(sum([self.field[self.SIZE-1-i][i] for i in range(self.SIZE)]))
        if abs(right_cross) == self.TO_WIN:
            return True

        return False

    def all_occupied(self):
        none_exists = not any([
            any([symbol == Symbol.NONE for symbol in row])
            for row in self.field
        ])
        return none_exists

    def render(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                symbol = self.field[i][j]
                if symbol == Symbol.CROSS:
                    print('X', end='')
                elif symbol == Symbol.ZERO:
                    print('O', end='')
                elif symbol == Symbol.NONE:
                    print(' ', end='')
            print()
