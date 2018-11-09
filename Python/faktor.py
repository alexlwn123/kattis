import sys
line = sys.stdin.readline().split()
n = int(line[0]) * int(line[1])
n -= int(line[0])-1
print(str(n))
