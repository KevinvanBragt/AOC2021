from unittest import TestCase

from input.input_parser import InputParser, OutputTypes
from shared.submarine.bingo.bingo_game_master import BingoGameMaster


class TestBingo(TestCase):

    def setUp(self) -> None:
        self.data = InputParser.get_input("day4_test", OutputTypes.List)
        self.bingo_game = BingoGameMaster(self.data)

    def test_bingo_setup(self):
        output = self.bingo_game.run()

        self.assertEqual(1924, output)
