import sys
print(len(set(x % 42 for x in list(map(int, sys.stdin.readlines())))))
