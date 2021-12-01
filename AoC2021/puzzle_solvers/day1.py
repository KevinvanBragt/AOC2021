from input.input_parser import InputParser, InputTypes
from shared.sonar_sweep import SonarSweep


class Day1:
    def solve(self):
        list = InputParser.get_input('day1', InputTypes.List)
        sweeper = SonarSweep([int(i) for i in list])
        return [sweeper.getMeasurementSlidingWindow(1), sweeper.getMeasurementSlidingWindow(3)]
