opps = (' // 4', ' + 4', ' * 4', ' - 4')

poss = ["4"]

for i in range(3):
    temp = []
    for x in poss:
        for op in opps:
            temp.append(x + op)
    poss = temp

solutions = {}
for x in poss:
    solutions[eval(x)] = x

cases = int(input())
for i in range(cases):
    val = int(input())

    if val in solutions:

        print(solutions[val].replace('//','/') + " = " + str(val))
    else:
        print('no solution')

