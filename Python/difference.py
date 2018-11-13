import sys

text = [int(x) for x in sys.stdin.read().split()]


for i in range(len(text) // 2):
	print(abs(text[int(2*i)] - text[int(2*i+1)]))