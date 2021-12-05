from unittest import TestCase

from shared.submarine.submarine_diagnostics import SubmarineDiagnostics


class TestSubmarineDiagnostics(TestCase):

    def setUp(self) -> None:
        self.data = ["00100", "11110", "10110", "10111", "10101",
                     "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
        self.sub_diagnostics = SubmarineDiagnostics(self.data)

    def test_epsilon_rate(self):
        self.assertEqual("01001", self.sub_diagnostics.epsilon_rating)

    def test_gamma_rate(self):
        self.assertEqual("10110", self.sub_diagnostics.gamma_rating)

    def test_o_rate(self):
        self.assertEqual("10111", self.sub_diagnostics.o2_rating)

    def test_co_rate(self):
        self.assertEqual("01010", self.sub_diagnostics.co2_rating)
