colsleft = [{i+1 for i in range(9)} for j in range(9)]
rowsleft = [{i+1 for i in range(9)} for j in range(9)]
sqleft =  [[{i+1 for i in range(9)} for j in range(3)] for k in range(3)]
board = [['.' for i in range(9)] for j in range(9)]

for i in range(9):
    line = input()
    for j in range(9):
        if line[j] != '.':
            print(line[j])
            board[i][j] = line[j]
            rowsleft[i].remove(int(line[j]))
            colsleft[j].remove(int(line[j]))
            sqleft[i//3][j//3].remove(int(line[j]))

for i in range(9):
    for j in range(9):
        setc = colsleft[j]
        setr = rowsleft[i]
        sets = sqleft[i//3][j//3]

        myset = setc & setr & sets

        if len(myset) == 1:
            board[i][j] = str(myset[0])
            x = myset[0]
            colsleft[j].remove(x)
            rowsleft[i].remove(x)
            sqlef[i//3][j//3].remove(x)


for line in board:
    print(''.join(line))

