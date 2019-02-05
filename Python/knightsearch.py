from collections import deque

goal = 'ICPCASIASG'
directions = [(2,-1), (2,1), (1, 2), (1,-2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

def dfs(word, r, c):
    global goal
    global board
    global directions

    if len(goal) == len(word):
        return True

    for dr, dc in directions:

        r1 = dr + r
        c1 = dc + c

        if r1 >= 0 and r1 < len(board) and c1 >= 0 and c1 < len(board):

            if goal.startswith(word + board[r1][c1]):
                if dfs(word+board[r1][c1], r1,c1):
                    return True
    return False

def main():
    n = int(raw_input())
    line = raw_input()
    global board
    board = [list(line[n*i:n*i+n]) for i in xrange(n)]

    for r0 in xrange(n):
        for c0 in xrange(n):
            if board[r0][c0] == 'I':
                if dfs('I', r0, c0):
                    print "YES"
                    return

    print "NO"




if __name__ == '__main__':
    main()
