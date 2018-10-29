import math
import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line[:-1]
for line in lines:
    line = line.split(" ")
    diff = []
    for i in range(len(line) -1):
        diff.append(abs(int(line[i]) - int(line[i+1])))
    joll = True
    for i in range(len(diff)-1):
        if i+1 not in diff:
            print('Not jolly')
            joll = False
            break
    if joll:
        print("Jolly")
