from utils.aoc_utils import AOCDay, day
from pprint import pprint


@day(5)
class Day5(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        return 0
    
    def parse_stacks(self, rows):
        stacks = [[],[],[],[],[],[],[],[],[]]
        for i in range(len(rows[-1].split('   '))):
            for j in rows:
                if (j == rows[-1]):
                    break
                value = j[i+1 + 3 * (i)]
                if value != ' ':
                    stacks[i].append(value)
        for i in stacks:
            i.reverse()
        return stacks
    
    def make_instruction(self, stacks, instruction):
        instr = []
        for i in instruction.split(' '):
            if i.isnumeric():
                instr.append(int(i))
        for i in range(instr[0]):
            if len(stacks[instr[1]-1]) > 0:
                stacks[instr[2]-1].append(stacks[instr[1]-1].pop())
        return stacks
    
    def make_instruction2(self, stacks, instruction):
        instr = []
        for i in instruction.split(' '):
            if i.isnumeric():
                instr.append(int(i))
        tmp_stk = []
        for i in range(instr[0]):
            tmp_stk.append(stacks[instr[1]-1].pop())
        tmp_stk.reverse() 
        for i in tmp_stk:
            stacks[instr[2]-1].append(i)
        return stacks



    def part1(self):
        i = self.rawData.split('\n\n')
        rows = i[0].split('\n')
        stacks = self.parse_stacks(rows)

        for j in i[1].split('\n'):
            stacks = self.make_instruction(stacks, j)
        res = ''
        for i in stacks:
            res += i.pop()

        return res

    def part2(self):
        i = self.rawData.split('\n\n')
        rows = i[0].split('\n')
        stacks = self.parse_stacks(rows)

        for j in i[1].split('\n'):
            stacks = self.make_instruction2(stacks, j)
        res = ''
        for i in stacks:
            res += i.pop()

        return res
