class HydroThermalVents:

    def __init__(self, line_data, size: int):
        self.size = size
        self.map = [[0 for _ in range(0, size)] for _ in range(0, size)]

        for line in line_data:
            self.draw_line(line)

    def draw_line(self, line: str):
        start_x, start_y = map(int, line.split('->')[0].strip().split(','))
        end_x, end_y = map(int, line.split('->')[1].strip().split(','))

        if start_y == end_y:
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                self.map[start_y][x] += 1
        elif start_x == end_x:
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                self.map[y][start_x] += 1
        else:
            range_x = range(start_x, end_x - 1, -1) if start_x > end_x else range(start_x, end_x + 1)
            range_y = range(start_y, end_y - 1, -1) if start_y > end_y else range(start_y, end_y + 1)
            for i, j in zip(range_y, range_x):
                self.map[i][j] += 1

    def print_map(self):
        print('map')
        for i in range(0, self.size):
            print(self.map[i], '\n')
        print('------------------------')

    def count(self):
        sum = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.map[i][j] >= 2:
                    sum += 1
        return sum

