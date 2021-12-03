from enum import Enum


class Command(Enum):
    forward = "forward",
    up = "up",
    down = "down"


class Position:

    def __init__(self, data):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.data = self.parseData(data)

    def parseData(self, data: [str]):
        return [(x.split()[0], x.split()[1]) for x in data]

    def calculateEndPoint(self) -> {}:
        for entry in self.data:
            match entry[0]:
                case 'forward':
                    self.horizontal += int(entry[1])
                    self.depth += int(entry[1])*self.aim
                case 'up':
                    self.aim -= int(entry[1])
                case 'down':
                    self.aim += int(entry[1])
        return {"depth": self.depth, "horizontal": self.horizontal}
