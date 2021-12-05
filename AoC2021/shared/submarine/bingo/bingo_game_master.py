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
        winner = None
        while winner is None:
            number_drawn = self.number_generator.draw_number()
            for board in self.boards:
                board.cross_if_exists(number_drawn)
                if board.has_bingo:
                    return self.get_puzzle_output(board, number_drawn)

    def get_puzzle_output(self, board: BingoBoard, number_drawn) -> int:
        return board.sum_remaining() * number_drawn
