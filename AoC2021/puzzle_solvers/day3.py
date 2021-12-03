from input.input_parser import InputParser, OutputTypes
from shared.submarine_diagnostics import SubmarineDiagnostics


class Day3:

    def __init__(self):
        self.data = InputParser.get_input("day3", OutputTypes.List)
        self.sub = SubmarineDiagnostics(self.data)

    def solve(self):
        rates = self.sub.get_life_support_ratings()
        o2 = int(rates["o"], 2)
        co2 = int(rates["co2"], 2)
        return o2 * co2
