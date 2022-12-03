from utils.aoc_utils import AOCDay, day


@day(3)
class Day3(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        return 0

    def part1(self):
        total_priority = 0
        for i in self.rawData.split('\n'):
            half = len(i) // 2
            rucksack1 = i[:half]
            rucksack2 = i[half:]
            for j in rucksack1:
                if j in rucksack2:
                    if j.isupper():
                        stonk = ord(j) - 38
                        if stonk > 52 or stonk < 27:
                            print("error")
                        total_priority += stonk
                    else:
                        stonk = ord(j) - 96
                        if stonk > 26 or stonk < 0:
                            print("error")
                        total_priority += stonk
                    break
        return total_priority
    def part2(self):
        total_priority = 0
        rucksack1 = ''
        rucksack2 = ''
        rucksack3 = ''
        for i in self.rawData.split('\n'):
            if (rucksack1 == ''):
                rucksack1 = i
                continue
            if (rucksack2 == ''):
                rucksack2 = i
                continue
            if (rucksack3 == ''):
                rucksack3 = i
            for j in rucksack1:
                if j in rucksack2 and j in rucksack3:
                    if j.isupper():
                        stonk = ord(j) - 38
                        if stonk > 52 or stonk < 27:
                            print("error")
                        total_priority += stonk
                    else:
                        stonk = ord(j) - 96
                        if stonk > 26 or stonk < 0:
                            print("error")
                        total_priority += stonk
                    rucksack1 = rucksack2 = rucksack3 = ''
                    break
        return total_priority
