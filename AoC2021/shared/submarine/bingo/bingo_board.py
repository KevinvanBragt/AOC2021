class BingoBoard:

    def __init__(self, data: [str]):
        self.data = [None] * 5
        self.has_bingo = False

        for index, row in enumerate(data):
            numbers = [int(str.strip(x)) for x in str.replace(row, '  ', ' ').split(' ') if x != '']
            self.data[index] = numbers

    def number_drawn(self, number: int):
        self.cross_if_exists(number)

    def cross_if_exists(self, number: int):
        for row in range(0, len(self.data)):
            for col in range(0, 5):
                if self.data[row][col] == number:
                    self.data[row][col] = None
                    self.check_is_winner(row, col)

    def check_is_winner(self, row, col):
        y = [self.data[y][col] for y in range(0, 5)]
        x = [self.data[row][x] for x in range(0, 5)]

        if y.count(None) == 5 or x.count(None) == 5:
            self.has_bingo = True

    def sum_remaining(self) -> int:
        sum = 0
        for row in range(0, len(self.data)):
            for col in range(0, 5):
                sum += self.data[row][col] if self.data[row][col] is not None else 0
        return sum


