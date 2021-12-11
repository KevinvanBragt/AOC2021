import collections


class BasinMap:
    coordinate_tuple = collections.namedtuple('coordinate', ('x', 'y'))

    def __init__(self, data):
        self.data = data
        self.low_points: list[BasinMap.coordinate_tuple] = []
        self.basin_sizes = []
        self.find_lowest_points()

    def find_lowest_points(self) -> [coordinate_tuple]:
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[0])):
                if self.test_is_lowest_point(self.coordinate_tuple(x, y)):
                    self.low_points.append(self.coordinate_tuple(x, y))
                    self.find_basin_size(self.coordinate_tuple(x, y))

    def test_is_lowest_point(self, coordinate: coordinate_tuple) -> bool:
        value = self.data[coordinate.y][coordinate.x]
        if value == 9:
            return False
        elif value == 0:
            return True
        else:
            neighbor_values = []
            if coordinate.y - 1 >= 0:
                neighbor_values.append(self.data[coordinate.y - 1][coordinate.x])
            if coordinate.y + 1 < len(self.data):
                neighbor_values.append(self.data[coordinate.y + 1][coordinate.x])
            if coordinate.x - 1 >= 0:
                neighbor_values.append(self.data[coordinate.y][coordinate.x - 1])
            if coordinate.x + 1 < len(self.data[0]):
                neighbor_values.append(self.data[coordinate.y][coordinate.x + 1])
            return value < min(neighbor_values)

    def find_basin_size(self, coordinate: coordinate_tuple):
        basinQueue: [(int, int)] = [(coordinate.x, coordinate.y)]
        for c in basinQueue:
            x = c[0]
            y = c[1]
            if y - 1 >= 0 and self.data[y - 1][x] != 9 and (x, y-1) not in basinQueue:
                basinQueue.append((x, y - 1))
            if y + 1 < len(self.data) and self.data[y + 1][x] != 9 and (x, y+1) not in basinQueue:
                basinQueue.append(self.coordinate_tuple(x, y + 1))
            if x - 1 >= 0 and self.data[y][x - 1] != 9 and (x-1, y) not in basinQueue:
                basinQueue.append(self.coordinate_tuple(x - 1, y))
            if x + 1 < len(self.data[0]) and self.data[y][x + 1] != 9 and (x+1, y) not in basinQueue:
                basinQueue.append(self.coordinate_tuple(x + 1, y))
        self.basin_sizes.append(len(basinQueue))

    """ part 1 """
    def sum_risk_score(self):
        return sum(list([self.data[c.y][c.x] + 1 for c in self.low_points]))

    """ part 2 """
    def multiply_largest_areas(self):
        self.basin_sizes.sort()
        return self.basin_sizes[-1] * self.basin_sizes[-2] * self.basin_sizes[-3]
