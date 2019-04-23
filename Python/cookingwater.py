def main():
  n = int(input())
  a, b = map(int, input().split())
  times = set([i for i in range(a,b+1)])
  for _ in range(n-1):
    a, b = map(int, input().split())
    temp = set([i for i in range(a, b+1)])

    times = (times & temp)
  print ("gunilla has a point" if len(times) else "edward is right")

if __name__ == '__main__':
  main()
