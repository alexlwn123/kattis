import sys

deck = set()

line = str(sys.stdin.readline())

for i in range(len(line) // 3):
	if (line[i*3: i*3+3]) in deck:	
		print("GRESKA")
		break
	else:
		deck.add(line[i*3:i*3+3])
else:
	
	P = sum(1 for x in deck if x.startswith('P'))
	K = sum(1 for x in deck if x.startswith('K'))
	H = sum(1 for x in deck if x.startswith('H'))
	T = sum(1 for x in deck if x.startswith('T'))

	print(13-P, 13-K, 13-H, 13-T)

