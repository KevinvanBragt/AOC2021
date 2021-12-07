from unittest import TestCase

from shared.submarine.align_crabs import AlignCrabs


class TestAlignCrabs(TestCase):

    def test_example_case_constant_costs(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        position, least_sum = AlignCrabs.get_least_distance(data, increasing_costs=False)
        self.assertEqual(position, 2)
        self.assertEqual(least_sum, 37)

    def test_example_case_increasing_costs(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        position, least_sum = AlignCrabs.get_least_distance(data, increasing_costs=True)
        self.assertEqual(position, 5)
        self.assertEqual(least_sum, 168)
