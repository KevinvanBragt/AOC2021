from input.input_parser import InputParser, OutputTypes
from shared.submarine.bingo.bingo_game_master import BingoGameMaster
from shared.submarine.submarine_diagnostics import SubmarineDiagnostics


class Day4:

    def __init__(self):
        self.data = InputParser.get_input("day4", OutputTypes.List)
        self.bingo_game = BingoGameMaster(self.data)

    def solve(self):
        return self.bingo_game.run()
