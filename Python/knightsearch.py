def main():
    width = int(input())
    line = input()
    board = [[" " for j in range(width)] for i in range(width)]

    for i in range(width):
        for j in range(width):
            board[i][j] = Node(line[(i*width) + j: i*width +j+1])
    directions = ((1,2), (1,-2), (2,1), (2,-1), (-2,-1), (-2,1), (-1,2), (-1,-2))
    starts = []
    for i in range(width):
        for j in range(width):
            if board[i][j].char == 'I':
                starts.append((i,j))
            for direction in directions:
                adjrow = direction[0] + i
                adjcol = direction[1] + j


                if (adjrow >= 0 and adjrow < width and adjcol >= 0 and adjcol < width):
                    board[i][j].neighbors.append(board[adjrow][adjcol])
    match = 'ICPCASIASG'
    for start in starts:
        ind = 1
        q = [board[start[0]][start[1]]]
        while len(q) > 0:
            if ind >= len(match):
                print('YES')
                return
            for neighbor in q[0].neighbors:
                if neighbor.char == match[ind]:
                    q.append(neighbor)
            del q[0]
            ind +=1
    if ind >= len(match): print('YES')
    else: print('NO')



class Node:

    def __init__(self, char=None):
        self.char = char
        self.neighbors = []

if __name__ == '__main__':
    main()
