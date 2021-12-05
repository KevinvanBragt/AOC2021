from unittest import TestCase

from shared.submarine.submarine_sonar import SonarSweep


class TestSonarSweep(TestCase):

    def setUp(self) -> None:
        self.data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.sonar_sweep = SonarSweep(self.data)

    def test_sonar_sweep_get_measurement_sliding_window_1(self):
        self.assertEqual(self.sonar_sweep.get_measurement_sliding_window(1), 7)

    def test_sonar_sweep_get_measurement_sliding_window_3(self):
        self.assertEqual(self.sonar_sweep.get_measurement_sliding_window(3), 5)
