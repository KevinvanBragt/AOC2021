from input.input_parser import InputParser, OutputTypes
from shared.submarine.lanternfish_population import LanternFishPopulation


class Day6:

    def __init__(self):
        data = InputParser.get_input("day6", OutputTypes.File)
        self.data = [int(x) for x in data.split(',')]

    def solve(self):
        pop = LanternFishPopulation(self.data)
        pop_count = pop.solve(256)
        return pop_count
