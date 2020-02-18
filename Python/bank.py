import sys
def main():
  lines = [x.strip() for x in sys.stdin.readlines()]
  N, T = map(int, lines[0].split())
  used = [False] * T
  people = sorted([tuple(map(int, x.split())) for x in lines[1:]], reverse=True)
  sum = 0
  
  for x in people: 
    time = x[1]
    good = True
    while time >= 0 and good:
      if used[time]:
        time -= 1
      else:
        sum += x[0]
        used[time] = True
        good = False
  print(sum)

if __name__ == '__main__':
  main()
