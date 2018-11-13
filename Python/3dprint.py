import math
import sys

n = int(sys.stdin.readline().strip())
if n == 0:
    print(0)
    exit()
i = 0
while 2 ** i < n:
    i += 1
print(i+1)





