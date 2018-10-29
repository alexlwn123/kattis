cases = int(input())
for j in range(cases):
    input()
    kids = int(input())
    sum = 0
    for i in range(kids):
        sum += int(input())
    if sum % kids == 0:
        print('YES')
    else:
        print('NO')

