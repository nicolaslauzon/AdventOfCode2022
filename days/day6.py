from utils.aoc_utils import AOCDay, day


@day(6)
class Day6(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        return 0
    def huhu(self, index):
        for i in range(len(self.rawData)-index):
            s = set(self.rawData[i:i+index])
            if len(s) == index:
                return i+index

    def part1(self):
        return self.huhu(4)


    def part2(self):
        return self.huhu(14)
