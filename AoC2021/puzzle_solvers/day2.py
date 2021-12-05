from input.input_parser import InputParser, OutputTypes
from shared.submarine.submarine_position import Position


class Day2:

    def __init__(self):
        self.data = InputParser.get_input("day2", OutputTypes.List)

    def solve(self) -> [int]:
        position = Position(self.data)
        positions = position.calculateEndPoint()
        return positions['depth'] * positions['horizontal']
