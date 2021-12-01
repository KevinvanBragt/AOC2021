from enum import Enum


class InputTypes(Enum):
    File = 1
    List = 2


class InputParser:
    @staticmethod
    def get_input(data: str, type: InputTypes = None):
        with open(f"input/data/{data}") as file:
            if type is None:
                    return file.read()
            elif type is InputTypes.List:
                    return [line for line in file.read().splitlines()]

