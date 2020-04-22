def main():
  s,t,n = map(int, input().split())
  d = list(map(int, input().split()))
  b = list(map(int, input().split()))
  c = list(map(int, input().split()))
  time = 0
  for i in range(n):
    time += d[i]
    time += (c[i] - (time % c[i])) %c[i] 
    time += b[i]

  time += d[-1]
  print('yes' if (t - s) >= time else 'no')




if __name__ == '__main__':
  main()
