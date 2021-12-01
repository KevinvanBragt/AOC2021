from tkinter.filedialog import Open

from input.puzzle_x_file import PuzzleXFile


class InputParser:
    @staticmethod
    def get_input(puzzle: PuzzleXFile):
        with Open(PuzzleXFile[puzzle]) as file:
            return file.Read()
