from enum import Enum


class Puzzle(Enum):
    Day1 = 1,
    Day2 = 2


class OutputTypes(Enum):
    File = 1
    List = 2


class InputParser:
    @staticmethod
    def get_input(data: str, output_type: OutputTypes = None):
        with open(f"C:\\Users\\kevin\\PycharmProjects\\AoC2021\\input\\data\\{data}") as file:
            if output_type is None or output_type is OutputTypes.File:
                return file.read()
            elif output_type is OutputTypes.List:
                return [line for line in file.read().splitlines()]
