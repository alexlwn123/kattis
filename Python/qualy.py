import sys
out = float(0)
n = int(sys.stdin.readline())
while n > 0:
    line = sys.stdin.readline().strip()
    line = line.split(' ')
    if len(line) == 2:
        out += float(line[0]) * float(line[1])
    n -= 1
print("%.3f" % out)
