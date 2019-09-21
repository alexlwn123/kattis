x, y = int(input()), int(input())

print(abs(y-x) if  y-x < 180 == y-x > 0 else abs(x-y) %180)


