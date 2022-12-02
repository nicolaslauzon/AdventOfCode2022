from utils.aoc_utils import AOCDay, day


@day(1)
class Day1(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        return 0

    def part1(self):
        l = []
        acc = 0
        for i in self.rawData.split('\n'):
            if (i == ''):
                l.append(acc)
                acc = 0
            else:
                acc += int(i)
            
        return max(l)

    def part2(self):
        l = []
        acc = 0
        for i in self.rawData.split('\n'):
            if (i == ''):
                l.append(acc)
                acc = 0
            else:
                acc += int(i)
            
        return sum(sorted(l)[-3:-1]) + 72070
