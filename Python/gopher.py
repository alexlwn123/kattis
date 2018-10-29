vals = input().split(' ')
for val in vals:
    val = int(val)
gophsn = val[0]
holesn = val[1]
time = val[2]
vel = val[3]

gophs = []
for i in range(gophsn):
    line = input().split(' ')
    gophs.append((float(line[0]), float(line[1])))

holes = []
for i in range(holesn)
