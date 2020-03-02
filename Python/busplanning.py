import sys
from collections import defaultdict
def main():
  n, k, c = map(int, sys.stdin.readline().strip().split())
  lines = sys.stdin.read().splitlines()
  kids = {x:set() for x in lines[:n]}
  for i in range(n, len(lines)):
    a, b = lines[i].split()
    kids[a].add(b)
    kids[b].add(a)
  
  busses = [set() for _ in range(17)]

  for kid in sorted(kids.keys(), key=lambda p: len(kids[p]), reverse=True):
    good = True
    i = 0
    
    while good and len(busses[i]) > 0:
      bus = busses[i]
      if len(bus) < c and len(kids[kid] & bus) == 0:
        bus.add(kid)
        good = False
      i+=1

    if good:
      busses[i].add(kid)

  count = sum([1 for x in busses if len(x)]) 
  
  print(count)
  for b in busses:
    if b:
      print(' '.join(b))

if __name__ == '__main__':
  main()
