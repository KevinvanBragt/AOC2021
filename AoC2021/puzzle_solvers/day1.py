from input.input_parser import InputParser, OutputTypes
from shared.submarine_sonar import SonarSweep


class Day1:
    def solve(self):
        list = InputParser.get_input('day1', OutputTypes.List)
        sweeper = SonarSweep([int(i) for i in list])
        return [sweeper.get_measurement_sliding_window(1), sweeper.get_measurement_sliding_window(3)]
