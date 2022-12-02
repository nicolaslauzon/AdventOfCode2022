from utils.aoc_utils import AOCDay, day


@day(2)
class Day2(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)

        return 0
        # Roche = 1 papier = 2 ciseau = 3
        # 0 = draw
        # 1 = win
        # 2 = lost
    def getWeigth(self, move):
        if (move == 'A' or move == 'X'):
            return 1
        elif (move == 'B' or move == 'Y'):
            return 2
        elif (move == 'C' or move == 'Z'):
            return 3
    
    def win(self, move):
        if (move == 'A'):
            return 2
        elif (move == 'B'):
            return 3
        elif (move == 'C'):
            return 1
    
    def loose(self, move):
        if (move == 'A'):
            return 3
        elif (move == 'B'):
            return 1
        elif (move == 'C'):
            return 2
    def part1(self):
        total_score = 0
        for i in self.rawData.split('\n'):
            moves = i.split(' ')
            if (len(moves) == 2):
                opp = moves[0]
                u = moves[1]
                res = 0
                res = self.getWeigth(u) - self.getWeigth(opp)
                if (res == 0):
                    total_score += 3
                elif (res == 1 or res == -2):
                    total_score += 6
                total_score += self.getWeigth(u)

        return total_score

    def part2(self):
        total_score = 0
        for i in self.rawData.split('\n'):
            moves = i.split(' ')
            if (len(moves) == 2):
                opp = moves[0]
                u = moves[1]
                
                if (u == 'Z'):
                    total_score += self.win(opp)
                    total_score += 6
                elif (u == 'Y'):
                    total_score += self.getWeigth(opp)
                    total_score += 3
                elif (u == 'X'):
                    total_score += self.loose(opp)
                    total_score += 0

        return total_score
