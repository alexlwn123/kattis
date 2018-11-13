import sys

line = sys.stdin.readline()
x = []
for word in line.split():
	x.append(int(word))

print((x[1] * 2 ) - x[0])




