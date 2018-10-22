import sys
from collections import defaultdict
def main():
    lines = sys.stdin.read().splitlines()
    case = 1
    while len(lines) > 0:
        CaseMap = []
        LineNum = lines[0].split(' ')

        CaseMap = lines[:int(LineNum[0])+1]
        lines = lines[int(LineNum[0])+1:]

        unionFind(CaseMap)
        print('Case ' + str(case) + ": " + str(unionFind(CaseMap)))
        case += 1

def unionFind(lines):
    caseNum = 0

    line = lines[0].split(' ')
    rows = int(line[0])
    colls = int(line[1])

    #print(str(rows) + str(colls))

    graph = [colls * [node()] for i in range(rows)]

    for i in range(rows):
        line = lines[i+1]
        for j in range(len(line)):
            graph[i][j] = node(line[j])

    directions = { (0, -1), (-1, 0), (0, 1), (1, 0) }
    for i in range(rows):
        for j in range(colls):

            if graph[i][j].pix == '-':
                for direction in directions:
                    adjrow = i + direction[0]
                    adjcol = j + direction[1]

     #               print(str(adjrow) + " " + str(adjcol) + " " + graph[adjrow][adjcol])

                    if adjrow >= 0 and adjrow < rows and adjcol >= 0 and adjcol < colls:

                        if graph[adjrow][adjcol].pix == '-':
                            graph[i][j].neighbors.append(graph[adjrow][adjcol])

    numstars = 0
    fog i in range(rows):
       for j in range(colls):

           if graph[i][j].pix == '-' and not graph[i][j].visited:
               numstars += 1
               graph[i][j].doDFS()


    return numstars




class node:
    def __init__(self, pix = None):
        self.visited = False
        self.neighbors = []
        self.pix = pix


    def doDFS(self):
        #print(self.neighbors)
        if self.visited:
            return
        self.visited = True
        for neighbor in self.neighbors:
            neighbor.doDFS()




if __name__ == '__main__':
    main()
