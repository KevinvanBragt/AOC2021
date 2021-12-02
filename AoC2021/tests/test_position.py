from unittest import TestCase

from shared.position import Position


class TestPosition(TestCase):

    def setUp(self) -> None:
        self.data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    def test_depth_should_be_correct(self):
        position = Position(self.data)
        positions = position.calculateEndPoint()
        self.assertEqual(60, positions["depth"])

    def test_horizontal_should_be_correct(self):
        position = Position(self.data)
        positions = position.calculateEndPoint()
        self.assertEqual(15, positions["horizontal"])
