from unittest import TestCase

from input.input_parser import OutputTypes, InputParser
from shared.submarine.hydrothermal_vents import HydroThermalVents


class TestHydrothermalVents(TestCase):

    def setUp(self) -> None:
        self.data = InputParser.get_input("day5_test", OutputTypes.List)
        self.htv = HydroThermalVents(self.data, 10)

    def test_htv(self):
        self.assertEqual(12, self.htv.count())
