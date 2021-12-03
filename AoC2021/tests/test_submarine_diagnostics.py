from unittest import TestCase

from shared.submarine_diagnostics import SubmarineDiagnostics


class TestSubmarineDiagnostics(TestCase):

    def setUp(self) -> None:
        self.data = ["00100", "11110", "10110", "10111", "10101",
                     "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
        self.sub_diagnostics = SubmarineDiagnostics(self.data)
        self.rates = self.sub_diagnostics.getRates()
        self.life_rates = self.sub_diagnostics.get_life_support_ratings()

    def test_epsilon_rate(self):
        self.assertEqual("01001", self.rates["epsilon"])

    def test_gamma_rate(self):
        self.assertEqual("10110", self.rates["gamma"])

    def test_o_rate(self):
        self.assertEqual(23, int(self.life_rates["o"], 2))

    def test_co_rate(self):
        self.assertEqual(10, int(self.life_rates["co2"], 2))
