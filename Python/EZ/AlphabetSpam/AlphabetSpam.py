import sys
import re

line = sys.stdin.readline()
line = line[:len(line)-1]


length = len(line)


up = sum(1 for c in line if c.isupper())
low = sum(1 for c in line if c.islower())
white = sum(1 for c in line if c == '_')
sym = length - (up + low + white)

print(white / length)
print(low / length)
print(up / length)
print(sym / length)