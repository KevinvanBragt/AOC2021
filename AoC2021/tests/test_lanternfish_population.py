from unittest import TestCase

from shared.submarine.lanternfish_population import LanternFishPopulation


class TestLanternFishPopulation(TestCase):

    def test_lanternfish_population_model_a(self):
        self.data = [3, 4, 3, 1, 2]
        pop = LanternFishPopulation(self.data)
        pop_count = pop.solve(18)
        self.assertEqual(26, pop_count)

    def test_lanternfish_population_model_b(self):
        self.data = [3, 4, 3, 1, 2]
        pop = LanternFishPopulation(self.data)
        pop_count = pop.solve(80)
        self.assertEqual(5934, pop_count)

    def test_lanternfish_population_model_c(self):
        self.data = [3, 4, 3, 1, 2]
        pop = LanternFishPopulation(self.data)
        pop_count = pop.solve(256)
        self.assertEqual(26984457539, pop_count)


