import sys
from collections import deque

def main():
  lines = iter(sys.stdin.read().splitlines())
  N = int(next(lines))
  if N == 1:
    print(next(lines))
    return
  nums = [[] for i in range(N)]
  words = [next(lines) for _ in range(N)]
  a, b = 0, 0 
  for _ in range(N-1):
    a, b = map(int, next(lines).split())
    nums[a-1].append(b-1)

  used = [False] * N 
  used[a-1] = True
  Q = deque([a-1])
  out = []

  while Q:
    curr = Q.popleft()
    out.append(words[curr])
    for x in nums[curr][::-1]:
      Q.appendleft(x) 


  print(''.join(out))


  

if __name__ == '__main__':
  main()
