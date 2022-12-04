from utils.aoc_utils import AOCDay, day


@day(4)
class Day4(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        return 0
    
    def contains(self, b1, e1, b2, e2):
        return (b1 <= b2 and e1 >= e2) or (b2 <= b1 and e2 >= e1)

    def overlap(self, b1, e1, b2, e2):
        return (b1 <= b2 and e1 >= b2) or (b2 <= b1 and e2 >= b1)

    def part1(self):
        total = 0
        index = 0
        for i in self.rawData.split('\n'):
            ranges = i.split(',')
            range1 = ranges[0].split('-')
            b1 = int(range1[0])
            e1 = int(range1[1])
            range2 = ranges[1].split('-')
            b2 = int(range2[0])
            e2 = int(range2[1])

            if (self.contains(b1,e1,b2,e2)):
                total += 1
            index += 1



        return total

    def part2(self):
        total = 0
        index = 0
        for i in self.rawData.split('\n'):
            ranges = i.split(',')
            range1 = ranges[0].split('-')
            b1 = int(range1[0])
            e1 = int(range1[1])
            range2 = ranges[1].split('-')
            b2 = int(range2[0])
            e2 = int(range2[1])

            if (self.overlap(b1,e1,b2,e2)):
                total += 1
            index += 1
        return total
