import sys
line = sys.stdin.readline().split()
line[0], line[1] = line[0][::-1], line[1][::-1]
map(int, line)
print(str(max(line[0],line[1])))
