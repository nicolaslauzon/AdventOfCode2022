from utils.aoc_utils import AOCDay, day


@day(8)
class Day8(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        return 0
    
    def is_hidden(self, i, j, lines):
        t_h = b_h = l_h = r_h = False
        for top in range(0, i):
            if (lines[top][j] >= lines[i][j]):
                t_h = True
                break
        for bottom in range(i+1, 99):
            if (lines[bottom][j] >= lines[i][j]):
                b_h = True
                break
        for left in range(0, j):
            if (lines[i][left] >= lines[i][j]):
                l_h = True
                break
        for right in range(j+1, 99):
            if (lines[i][right] >= lines[i][j]):
                r_h = True
                break
        return (t_h and b_h and l_h and r_h)
    
    def compute_scenic_score(self, i, j, lines):

        t_s = b_s = l_s = r_s = 0
        for top in range(i-1, -1, -1):
            t_s += 1
            if (lines[top][j] >= lines[i][j]):
                break
        for bottom in range(i+1, 99):
            b_s += 1
            if (lines[bottom][j] >= lines[i][j]):
                break
        for left in range(j-1, -1, -1):
            l_s += 1
            if (lines[i][left] >= lines[i][j]):
                break
        for right in range(j+1, 99):
            r_s += 1
            if (lines[i][right] >= lines[i][j]):
                break
        return t_s * b_s * l_s * r_s


    def part1(self):
        hidden = 0
        lines = self.rawData.split('\n')
        for i in range(1, len(lines)-1):
            for j in range(1, len(lines[i])-1):
                if (self.is_hidden(i, j, lines)):
                    hidden += 1
        return len(self.rawData) - len(lines) + 1 - hidden


    def part2(self):
        best = 0
        lines = self.rawData.split('\n')
        for i in range(1, len(lines)-1):
            for j in range(1, len(lines[i])-1):
                curr = self.compute_scenic_score(i, j, lines)
                if (curr > best):
                    best = curr
        return best
