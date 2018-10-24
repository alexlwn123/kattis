import sys

def main():
    lines = sys.stdin.read().splitlines();
    line1 = lines[0].split(" ")
    height = int(line1[0])
    width = int(line1[1])
    lines = lines[1:]
    lines.append(width * '0')
    lines.insert(0, width * '0')
    height += 2
    for i in range(len(lines)):
        lines[i] = '0' + str(lines[i]) + '0'
    width += 2
    for i in range(len(lines)):
        temp = []
        for j in range(len(lines[i])):
            temp.append(lines[i][j])
        lines[i] = temp
    graph = [[node() for j in range(width)] for i in range(height)]
    unionFind(graph, lines)


def unionFind(graph, lines):
    for i in range(len(graph)):
        for j in range(len(lines[i])):
            if lines[i][j] == '1':
                graph[i][j].land = True
    directions = {(0,1), (0, -1), (1, 0), (-1, 0)}


    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for direction in directions:
                adjrow = i + direction[0]
                adjcol = j + direction[1]

                if adjrow >= 0 and adjcol >= 0 and adjrow < len(graph) and adjcol < len(graph[i]):
                    if graph[i][j].land == graph[adjrow][adjcol].land:
                        graph[i][j].neighbors.append(graph[adjrow][adjcol])

    graph[0][0].doDFS() #oceans
    #counting
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j].land:
                for direction in directions:
                    adjrow = i + direction[0]
                    adjcol = j + direction[1]

                    if adjrow >= 0 and adjcol >= 0 and adjrow < len(graph) and adjcol < len(graph[i]):

                        if graph[adjrow][adjcol].ocean:
                            count += 1

    print(str(count))





class node:

    def __init__(self):
        self.land = False
        self.neighbors = []
        self.ocean = False

    def __str__(self):
       return str(self.land) + " " + str(len(self.neighbors)) + str(self.ocean)
    __repr__ = __str__

    def doDFS(self):
        if self.ocean:
            return
        self.ocean = True
        for neighbor in self.neighbors:
            neighbor.doDFS();

if __name__ == '__main__':
    main()
