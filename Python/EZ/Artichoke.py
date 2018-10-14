import sys
import math
def main():
	line = sys.stdin.readline().split(" ");
	
	nums = list(map(int, line))
	p = nums[0]
	a = nums[1]
	b = nums[2]
	c = nums[3]
	d = nums[4]
	n = nums[5]

	maxDrop = 0;
	maxVal = (p * (math.sin(a + b) + math.cos(c + d) + 2))
	
	for i in range(2, n+1):
		nextVal = (p * (math.sin(a * i + b) + math.cos(c * i + d) + 2))

		if maxVal < nextVal:
			maxVal = nextVal

		elif maxVal - nextVal > maxDrop:
			maxDrop = maxVal - nextVal

	print('{:.9f}'.format(maxDrop))

if __name__ == '__main__':
	main()