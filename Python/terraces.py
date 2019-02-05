def find(arr, x):
    if arr[x] == x:
        return x
    arr[x] = find(arr, arr[x])
    return arr[x]

def union(arr, x, y):
    arr[find(arr, x)] = find(arr, y)

def main():
    width, height = map(int, input().split())
    board = []

    canFlow = [False for _ in range(width*height)]

    for _ in range(height):
        board.append(list(map(int, input().split())))
    uf = [i for i in range(width*height)]

    for i in range(height):
        for j in range(width):

            if j < width-1:
                if board[i][j] == board[i][j+1]:
                    union(uf, i*width + j, i * width + j + 1)

            if i < height-1:
                if board[i][j] == board[i+1][j]:
                    union(uf, i*width+j, (i+1)*width + j)

    for i in range(height):
        for j in range(width):

            if j > 0:
                if board[i][j] > board[i][j-1]:
                    canFlow[find(uf, uf[i*width+j])] = True

            if i > 0:
                if board[i][j] > board[i-1][j]:
                    canFlow[find(uf, uf[i*width+j])] = True


            if j < width-1:
                if board[i][j] > board[i][j+1]:
                    canFlow[find(uf, uf[i * width+j])] = True

            if i < height-1:
                if board[i][j] > board[i+1][j]:
                    canFlow[find(uf, uf[i*width+j])] = True

    count = 0
    for i in range(width*height):
        if not canFlow[find(uf, i)]:
            count +=1

    print(count)

if __name__ == '__main__':
    main()

