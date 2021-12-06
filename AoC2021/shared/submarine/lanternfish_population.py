class LanternFishPopulation:

    def __init__(self, initial_population: [int]):
        # key is time_left, value = nr_fish
        self.population = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for x in initial_population:
            self.population[x] += 1

    def solve(self, nr_of_days: int) -> int:
        day = 0
        while day < nr_of_days:
            self.next_day()
            day += 1
        return self.count_total_population()

    def next_day(self):
        births = self.population[0]

        self.population[0] = self.population[1]
        self.population[1] = self.population[2]
        self.population[2] = self.population[3]
        self.population[3] = self.population[4]
        self.population[4] = self.population[5]
        self.population[5] = self.population[6]
        self.population[6] = self.population[7] + births
        self.population[7] = self.population[8]
        self.population[8] = births

    def count_total_population(self) -> int:
        return sum([value for _, value in self.population.items()])
