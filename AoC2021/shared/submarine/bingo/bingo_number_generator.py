class BingoNumberGenerator:

    def __init__(self, data: [str]):
        self.numbers = [int(number) for number in str.split(data[0], ',')]
        self.iterator = iter(self.numbers)

    def draw_number(self):
        return next(self.iterator)



