import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line[:-1]
speed = 0
distance = 0
prevtime = [0,0,0]
for line in lines:
    line = line.split(" ")
    time = line[0].split(':')
    time = [int(x) for x in time]
    changetime = [time[0] - prevtime[0], time[1] - prevtime[1], time[2] - prevtime[2]]
    distance += changetime[0] * speed
    distance += changetime[1] * speed / 60
    distance += changetime[2] * speed / 3600
    prevtime = [time[0], time[1], time[2]]
    if len(line) == 2:
        speed = int(line[1])

    if len(line) == 1:
        print(line[0][:-1] + " " + "%.2f" % distance + " km")
