from enum import Enum


class Puzzle(Enum):
    Day1 = 1,
    Day2 = 2


class OutputTypes(Enum):
    File = 1
    List = 2


class InputParser:
    @staticmethod
    def get_input(file_name: str, output_type: OutputTypes = None, addition_parse_function = None):
        with open(f"C:\\Users\\kevin\\PycharmProjects\\AoC2021\\input\\data\\{file_name}") as file:
            if output_type is None or output_type is OutputTypes.File:
                return file.read()
            elif output_type is OutputTypes.List and addition_parse_function is None:
                return [line for line in file.read().splitlines()]
            elif output_type is OutputTypes.List and addition_parse_function is not None:
                return [addition_parse_function(x) for x in [line for line in file.read().splitlines()]]