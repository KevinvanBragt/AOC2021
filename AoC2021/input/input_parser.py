from enum import Enum


class Puzzle(Enum):
    Day1 = 1,
    Day2 = 2


class InputTypes(Enum):
    File = 1
    List = 2


class InputParser:
    @staticmethod
    def get_input(data: str, output_type: InputTypes = None):
        with open(f"input/data/{data}") as file:
            if output_type is None:
                return file.read()
            elif output_type is InputTypes.List:
                return [line for line in file.read().splitlines()]
