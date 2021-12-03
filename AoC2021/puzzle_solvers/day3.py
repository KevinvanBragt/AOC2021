from input.input_parser import InputParser, OutputTypes
from shared.submarine_diagnostics import SubmarineDiagnostics


class Day3:

    def __init__(self):
        self.data = InputParser.get_input("day3", OutputTypes.List)
        self.sub = SubmarineDiagnostics(self.data)

    def solve(self):
        o2 = int(self.sub.o2_rating, 2)
        co2 = int(self.sub.co2_rating, 2)
        return o2 * co2
