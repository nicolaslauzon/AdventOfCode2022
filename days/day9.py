from utils.aoc_utils import AOCDay, day
from copy import deepcopy


@day(9)
class Day9(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        self.board = [[False for i in range(1000)] for i in range(1000)]
        self.board[4][0] = True
        self.position_head = [4, 0]
        self.position_tail = [4, 0]

        self.last_move = 0
        self.last_head_pos = [0, 0]

        self.board2 = [[False for i in range(1000)] for i in range(1000)]
        self.board2[4][0] = True
        self.position_head2 = [4, 0]
        self.last_move2 = [0 for i in range(9)]
        self.last_head_pos2 = [[0, 0] for i in range(9)]
        self.position_tail2 = [[4, 0] for i in range(9)]
        return 0
    
    def is_adjacent(self, head, tail):
        diff_y = abs(head[0] - tail[0])
        diff_x = abs(head[1] - tail[1])
        if (diff_x > 1 or diff_y > 1):
            return False
        return True
    
    def move_tail(self, head, tail):
        for i in range(len(head)):
            if (head[i] == tail[i]):
                tail[(i+1)%2] += self.last_move
                return tail
        tail = deepcopy(self.last_head_pos)
        return tail

    def move_tail2(self, head, tail, tail_index):
        if (tail_index > 0):
            self.last_head_pos2[tail_index] = deepcopy(tail)

        for i in range(len(head)):
            if (head[i] == tail[i]):
                tail[(i+1)%2] += self.last_move2[tail_index-1]
                return tail
        tail = deepcopy(self.last_head_pos2[tail_index-1])
        return tail
        
    def move_head(self, direction):
        self.last_head_pos = deepcopy(self.position_head)
        if direction == 'U':
            self.position_head[0] -= 1
            self.last_move = -1
        elif direction == 'D':
            self.position_head[0] += 1
            self.last_move = 1
        elif direction == 'R':
            self.position_head[1] += 1
            self.last_move = 1
        elif direction == 'L':
            self.position_head[1] -= 1
            self.last_move = -1

    def move_head2(self, direction):
        self.last_head_pos2[0] = deepcopy(self.position_head2)
        if direction == 'U':
            self.position_head2[0] -= 1
            self.last_move2[0] = -1
        elif direction == 'D':
            self.position_head2[0] += 1
            self.last_move2[0] = 1
        elif direction == 'R':
            self.position_head2[1] += 1
            self.last_move2[0] = 1
        elif direction == 'L':
            self.position_head2[1] -= 1
            self.last_move2[0] = -1



    def part1(self):
#         self.rawData = '''R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2'''
        for i in self.rawData.split('\n'):
            direction, how_much = i.split(' ')
            for _ in range(int(how_much)):
                self.move_head(direction)
                if (not self.is_adjacent(self.position_head, self.position_tail)):
                    self.position_tail = self.move_tail(self.position_head, self.position_tail)
                    self.board[self.position_tail[0]][self.position_tail[1]] = True
                    
        total = 0
        for i in self.board:
            for j in i:
                if (j == True):
                    total += 1
        return total

    def part2(self):
        for i in self.rawData.split('\n'):
            direction, how_much = i.split(' ')
            for _ in range(int(how_much)):
                self.move_head2(direction)
                for j in range(9):
                    tmp_head = self.position_head2
                    if j > 0:
                        tmp_head = self.position_tail2[j-1]

                    if (not self.is_adjacent(tmp_head, self.position_tail2[j])):

                        self.position_tail2 = self.move_tail2(tmp_head, self.position_tail2[j], j)

                        self.board2[self.position_tail2[-1][0]][self.position_tail2[-1][1]] = True
                    
        total = 0
        for i in self.board2:
            for j in i:
                if (j == True):
                    total += 1
        return total
