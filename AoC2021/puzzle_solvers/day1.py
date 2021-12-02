from input.input_parser import InputParser, OutputTypes
from shared.sonar_sweep import SonarSweep


class Day1:
    def solve(self):
        list = InputParser.get_input('day1', OutputTypes.List)
        sweeper = SonarSweep([int(i) for i in list])
        return [sweeper.getMeasurementSlidingWindow(1), sweeper.getMeasurementSlidingWindow(3)]
