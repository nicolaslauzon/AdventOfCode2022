from utils.aoc_utils import AOCDay, day


@day(7)
class Day7(AOCDay):
    def common(self):
        # print(self.inputData)
        # print(self.rawData)
        return 0

    def part1(self):
        root_dir = self.parse_input()
        # root_dir.print_tree()
        print(root_dir.depth_search())

    def part2(self):
        root_dir = self.parse_input()
        # root_dir.print_tree()
        print(root_dir.depth_search())
        print(root_dir.size)
        return root_dir.part2(999999999999999,30000000- (70000000-root_dir.size))

    def parse_input(self):
        root_dir = Dir('/', 0)
        current_dir = root_dir
        for i in self.rawData.split('\n'):
            command = i.split(' ')
            if i[0] == '$':
                if i == '$ cd ..':
                    # for i in current_dir.getChilds():
                    #     current_dir.size += i.size
                    current_dir = current_dir.getParent()
                elif len(command) == 3:
                    current_dir = current_dir.getChild(command[2])

            elif command[0] == 'dir':
                current_dir.addChild(command[1], 0)
            else:
                current_dir.size += int(command[0])
            
        return root_dir


class Dir:
    def __init__(self, name, size):
        self.childs = []
        self.name = name
        self.size = size
        self.parent = None

    def addChild(self, name, size):
        new_node = Dir(name, size)
        new_node.parent = self
        self.childs.append(new_node)

    def getParent(self):
        return self.parent 
    
    def getChilds(self):
        return self.childs
    
    def getChild(self, name):
        for i in self.childs:
            if i.name == name:
                return i

    def print_tree(self, tabulation = ''):
        print(tabulation + self.name + f' ( {self.size} )')
        for i in self.getChilds():
            i.print_tree(tabulation + '  ')
    
    def depth_search(self):
        ans = 0
        for i in self.getChilds():
            s, a = i.depth_search()
            self.size += s
            ans += a
        if self.size <= 100000:
            ans += self.size
        return (self.size, ans)
    
    def part2(self, minimum, to_free):
        for i in self.getChilds():
            minimum = i.part2(minimum, to_free)
        if self.size >= to_free and self.size < minimum:
            minimum = self.size
        return minimum
