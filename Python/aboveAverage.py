import sys

n = int(sys.stdin.readline())

for i in range(n):
	line = sys.stdin.readline().split(" ")
	avg = float(sum(int(x) for x in line[1:])) / float(line[0])
	#print(avg)
	avgabove = float(sum(1 for x in line[1:] if float(x) > avg)) / float(line[0])
	print('%.3f' % (avgabove * 100) + "%")
