class SubmarineDiagnostics:

    def __init__(self, data: [str]):
        self.data: [str] = data

    def getRates(self):
        epsilon = ""  # least common
        gamma = ""  # most common
        data = [list(i) for i in self.data]

        for col in range(0, len(data[0])):
            avg = self.get_column_bit_average(col, data)
            gamma += '0' if avg < 0.5 else '1'
            epsilon += '0' if avg > 0.5 else '1'
        return {"gamma": gamma, "epsilon": epsilon}

    def get_column_bit_average(self, col, data):
        total = 0
        for row in range(0, len(data)):
            total += int(data[row][col])

        return total/len(data)

    def get_life_support_ratings(self):
        data = list.copy(self.data)
        i = 0
        while len(data) != 1:
            avg = self.get_column_bit_average(i, data)
            gamma = '0' if avg < 0.5 else '1'
            data = list(filter(lambda d: d[i] == gamma, data))
            i += 1
        o = data[0]

        data = list.copy(self.data)
        i = 0
        while len(data) != 1:
            avg = self.get_column_bit_average(i, data)
            epsilon = '0' if avg >= 0.5 else '1'
            data = list(filter(lambda d: d[i] == epsilon, data))
            i += 1
        co2 = data[0]

        return {"o": o, "co2": co2}
