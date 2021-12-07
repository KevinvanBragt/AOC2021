from input.input_parser import InputParser, OutputTypes
from shared.submarine.align_crabs import AlignCrabs


class Day7:

    @staticmethod
    def solve():
        data = InputParser.get_input("day7", OutputTypes.File)
        data = [int(x) for x in data.split(',')]
        pos, cost = AlignCrabs.get_least_distance(data, increasing_costs=True)
        print(cost)