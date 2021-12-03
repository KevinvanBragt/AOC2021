class SonarSweep:
    data: []

    def __init__(self, data):
        self.data = [x for x in data]

    def get_measurement_sliding_window(self, measurement: int):
        subsets = [self.data[i:i + measurement] for i in range(0, len(self.data)-measurement+1)]
        return sum(1 for i in range(0, len(subsets)-1) if sum(subsets[i+1]) > sum(subsets[i]))
