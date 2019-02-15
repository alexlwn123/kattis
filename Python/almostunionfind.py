class AlmostUF:
    def __init__(self, nodes):
        self.nodes = nodes
        self.sets = [{i} for i in xrange(nodes+1)]
        self.set_map = [i for i in xrange(nodes+1)]

    def union(self, x, y):
        if self.same(x,y):
            return
        if len(self.sets[self.set_map[x]]) < len(self.sets[self.set_map[y]]):
            self.moveAll(x, y)
        else:
            self.moveAll(y,x)
    def same(self, x, y):
        return self.set_map[x] == self.set_map[y]


    def move(self, x, y):
        if self.same(x, y):
            return
        self.sets[self.set_map[x]].discard(x)
        self.sets[self.set_map[y]].add(x)
        self.set_map[x] = self.set_map[y]

    def moveAll(self, x, y):
        if self.same(x, y):
            return

        old = self.set_map[x]
        new = self.set_map[y]

        for elem in self.sets[old]:
            self.set_map[elem] = new
            self.sets[new].add(elem)

        self.sets[old].clear()


def main():
    while True:
        try:
            nodes, commands = map(int, raw_input().split())
            ob = AlmostUF(nodes)

            for _ in xrange(commands):
                line = list(map(int, raw_input().split()))

                if line[0] == 1:
                    ob.union(line[1], line[2])
                elif line[0] == 2:
                    ob.move(line[1], line[2])
                else:
                    size = len(ob.sets[ob.set_map[line[1]]])
                    print size, sum(ob.sets[ob.set_map[line[1]]])

        except EOFError:
            break


if __name__ == '__main__':
    main()

