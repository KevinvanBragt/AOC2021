from input.input_parser import InputParser, OutputTypes
from shared.submarine.hydrothermal_vents import HydroThermalVents


class Day5:

    def __init__(self):
        self.data = InputParser.get_input("day5", OutputTypes.List)
        self.htv = HydroThermalVents(self.data, 1000)

    def solve(self) -> int:
        return self.htv.count()
