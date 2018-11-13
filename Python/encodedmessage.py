import sys
import math
n = int(sys.stdin.readline())

for i in range(n):
	line = str(sys.stdin.readline())
	size = int(math.sqrt(len(line)))
	board = [[0] * size] * size
	for j in range(size):
		for k in range(size):
			board[j][k] = line[j+k]
	out = ""
	for j in range(size):
		for k in range(size):
			print(k)
			
			out = str(out) + str(board[size-k-1][j])
	print(out)
