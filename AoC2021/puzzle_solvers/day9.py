from input.input_parser import InputParser, OutputTypes
from shared.basin_map import BasinMap


class Day9:

    @staticmethod
    def solve() -> int:
        data = InputParser.get_input("day9", OutputTypes.List, Day9.parse_function)
        basin_map = BasinMap(data)
        return basin_map.multiply_largest_areas()


    @staticmethod
    def parse_function(line: str):
        return [int(x) for x in list(line)]
