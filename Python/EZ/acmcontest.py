import sys
lines = sys.stdin.readlines()
lines = lines[:-1]
time = 0
points = 0
questions = {}
for eachline in lines:
	line = eachline.split(" ")


	
	
	line[2] = line[2][:-1]
	#print(line)

	if line[2] == "wrong":
		
		if line[1] in questions:
			questions[line[1]] += 20
		else:
			questions.update({line[1] : 20})
	if line[2] == "right":
		#print("right " + line[0] + str(time))
		points += 1
		time += int(line[0])
		if line[1] in questions:
			
			time += questions.get(line[1])

print(str(points) + " " + str(time))