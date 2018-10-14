import sys

info = sys.stdin.readline().split(" ")
info[1] = info[1][:-1]
print(info)

rooms = [False for i in range(int(info[0]))]


if int(info[1]) >= int(info[0]):
	print("too late")
	exit()

for x in info:
	rooms[int(x)-1] = True

for i in range(len(rooms)):
	if not rooms[i]:
		print(str(rooms[i]))
		exit()



