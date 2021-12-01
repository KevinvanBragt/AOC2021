class SonarSweep:
    data: []
    elevation_diff = []

    def __init__(self, data):
        self.data = [x for x in data]
        self.sweep()

    def getElevationMap(self):
        return self.elevation_diff

    def getElevationMapPositiveCount(self):
        return [e for e in self.elevation_diff if e > 0].__len__()

    def sweep(self):
        self.elevation_diff = [self.data[i+1] - self.data[i] for i in range(0, self.data.__len__()-2)]
