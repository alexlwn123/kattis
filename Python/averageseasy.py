from heapq import heappush, heappop, heapify
def main():
  T = int(input())
  for _ in range(T):
    input()
    nc, ne = map(int, input().split(' '))
    c, e = [], []
    c = list(map(int, input().split(' ')))
    e = list(map(int, input().split(' ')))
    count = 0
    cav = sum(c) / len(c)
    eav = sum(e) / len(e)
    for i in range(nc):
      if c[i] < cav and c[i] > eav:
        count += 1

    print(count)



if __name__ == '__main__':
  main()
