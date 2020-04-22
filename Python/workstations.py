from heapq import heappush, heappop, heapify

def main():
  n, m = map(int, input().split())
  q = []
  for _ in range(n):
    heappush(q, tuple(map(int, input().split())))

  Q = [] 
  count = 0
  while q:
    curr = heappop(q)
    if not Q:
      heappush(Q, sum(curr))
      continue
    
    done = heappop(Q)
    l = []
    while curr[0] < done:
      l.append(done)
      if not Q:
        break
      done = heappop(Q)
    for elem in l:
      heappush(Q, elem)

      
    if curr[0] - done <= m:
      count+=1

    heappush(Q, sum(curr))

  print(count)



if __name__ == '__main__':
  main()
