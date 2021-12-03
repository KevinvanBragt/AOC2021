class SubmarineDiagnostics:

    def __init__(self, data: [str]):
        self.data: [str] = data

    @property
    def o2_rating(self):
        return self.get_o2_rating()

    @property
    def co2_rating(self):
        return self.get_co2_rating()

    @property
    def gamma_rating(self):
        return self.get_gamma_rating()

    @property
    def epsilon_rating(self):
        return self.get_epsilon_rating()

    def get_gamma_rating(self):
        gamma = ""
        data = [list(i) for i in self.data]
        for col in range(0, len(data[0])):
            avg = self.get_column_bit_average(col, data)
            gamma += '0' if avg < 0.5 else '1'
        return gamma

    def get_epsilon_rating(self):
        epsilon = ""
        data = [list(i) for i in self.data]

        for col in range(0, len(data[0])):
            avg = self.get_column_bit_average(col, data)
            epsilon += '0' if avg > 0.5 else '1'
        return epsilon

    def get_o2_rating(self):
        data = list.copy(self.data)
        i = 0
        while len(data) != 1:
            avg = self.get_column_bit_average(i, data)
            gamma = '0' if avg < 0.5 else '1'
            data = list(filter(lambda d: d[i] == gamma, data))
            i += 1
        return data[0]

    def get_co2_rating(self):
        data = list.copy(self.data)
        i = 0
        while len(data) != 1:
            avg = self.get_column_bit_average(i, data)
            epsilon = '0' if avg >= 0.5 else '1'
            data = list(filter(lambda d: d[i] == epsilon, data))
            i += 1
        return data[0]

    @staticmethod
    def get_column_bit_average(col, data):
        total = 0
        for row in range(0, len(data)):
            total += int(data[row][col])
        return total/len(data)
