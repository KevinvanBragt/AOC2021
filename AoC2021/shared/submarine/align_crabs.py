import functools
from statistics import mean


class AlignCrabs:

    @functools.cache
    @staticmethod
    def get_triangular_number(x: int):
        return x * (x + 1)/ 2

    @staticmethod
    def get_least_distance(data, increasing_costs: bool):
        least_sum = 999999999
        position = -1
        for i in range(0, max(data)):
            current_sum = sum(abs(x - i) for x in data) if not increasing_costs \
                else sum(AlignCrabs.get_triangular_number(abs(x - i)) for x in data)
            if current_sum < least_sum:
                least_sum = current_sum
                position = i

        return position, least_sum
