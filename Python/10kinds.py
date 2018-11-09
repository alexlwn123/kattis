def find(arr, x):
    if arr[x] == x:
        return x
    arr[x] = find(arr, arr[x])
    return arr[x]

def union(arr, x, y):
    arr[find(arr, x)] = find(arr, y)

def main():
    row, col = map(int, input().split())
    uf = [i for i in range(row*col)]
    board = []
    for i in range(row):
        board.append(input())

    for i in range(row):
        for j in range(col):
            if i < row-1 and board[i][j] == board[i+1][j]:
                x = i*col + j
                y = (i+1)*col + j
                union(uf, x, y)
            if j < col-1 and board[i][j] == board[i][j+1]:
                x = i*col + j
                y = i*col + j + 1
                union(uf, x, y)

    q = int(input())
    for i in range(q):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        x = a*col + b
        y = c*col + d
        if find(uf, x) == find(uf, y):
            if board[a][b] == '0':
                print('binary')
            else:
                print('decimal')
        else:
            print('neither')

if __name__ == "__main__":
    main()
