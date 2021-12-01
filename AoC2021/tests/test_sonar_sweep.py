from unittest import TestCase

from shared.sonar_sweep import SonarSweep


class TestSonarSweep(TestCase):

    def test_sonar_sweep_elevation_diff_correct_amount_of_up_down(self):
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        sonar_sweep = SonarSweep(data)
        self.assertTrue(sonar_sweep.getElevationMapPositiveCount(), 7)