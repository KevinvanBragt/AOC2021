from input.input_parser import InputParser
from input.puzzle_x_file import PuzzleXFile


class Day1:
    def solve(self):
        file = InputParser.get_input(PuzzleXFile.Day1a)

        for string in file:
            print(string)
