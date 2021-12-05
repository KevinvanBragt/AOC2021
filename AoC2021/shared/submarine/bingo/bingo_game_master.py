from shared.submarine.bingo.bingo_board import BingoBoard
from shared.submarine.bingo.bingo_number_generator import BingoNumberGenerator


class BingoGameMaster:

    def __init__(self, data: [str]):
        self.number_generator = BingoNumberGenerator(data)
        self.boards = []

        board_data = [data[line] for line in range(2, len(data)) if data[line] != ""]
        for i in range(0, len(board_data), 5):
            self.boards.append(BingoBoard(board_data[i:i + 5]))
            i += 5

    def run(self) -> int:
        nr_of_boards = len(self.boards)
        number_drawn = -1;
        while nr_of_boards > 1:
            number_drawn = self.number_generator.draw_number()
            for board in self.boards:
                board.cross_if_exists(number_drawn)
            self.boards = list(filter(lambda b: b.has_bingo is False, self.boards))
            nr_of_boards = len(self.boards)

        board = self.boards[0]
        while not board.has_bingo:
            number_drawn = self.number_generator.draw_number()
            board.cross_if_exists(number_drawn)

        return self.get_puzzle_output(board, number_drawn)


    def get_puzzle_output(self, board: BingoBoard, number_drawn) -> int:
        return board.sum_remaining() * number_drawn
