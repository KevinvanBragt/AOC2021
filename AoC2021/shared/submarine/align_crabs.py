import functools


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
                print('found better position: position=', position, ' distance=', least_sum)
            print('found position: position=', position, ' distance=', current_sum)

        return position, least_sum
