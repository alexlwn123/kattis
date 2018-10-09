import sys
def main(): 

	firstLine = sys.stdin.readline().split(" ")
	firstLine[2] = firstLine[2][:-1]

	height = int(firstLine[0])
	width = int(firstLine[1])
	bricks = int(firstLine[2])

	bricks = sys.stdin.readline().split(" ")
	bricks[len(bricks)-1] = bricks[len(bricks)-1][:-1]

	bricks = list(map(int, bricks))

	currentWidth = 0
	currentHeight = 0

	for brick in bricks:
		currentWidth += brick

		if currentWidth == width:
			currentWidth = 0
			currentHeight += 1
			if currentHeight == height:
				print('YES')
				sys.exit()
		elif currentWidth > width:
			print('NO')
			sys.exit()

	print('NO')




if __name__ == __name__:
	main()