cases = int(input())

for i in range(cases):
    teams = int(input())
    students = input().split(' ')
    students = [int(x) for x in students]
    students.sort()
    total = 0
    for j in range(teams):
        students.pop(0)
        students.pop(-1)
        total += students[-1]
        students.pop(-1)


    print(str(total))


