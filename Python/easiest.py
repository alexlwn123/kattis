import sys
def main():
  lines = list(map(int, sys.stdin.read().splitlines()))
  out = []
  for N in lines:
    bad = True
    goal = sum(list(map(int, list(str(N))))) 
    i = 11
    while sum(list(map(int, list(str(N * i))))) != goal:
      i+= 1

    out.append(str(i))

  del out[-1]



        
  print('\n'.join(out))









if __name__ == '__main__':
  main()

