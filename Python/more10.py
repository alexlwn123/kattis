import sys
from collections import defaultdict
def foo(X):
  return [x[max(-3, -len(x)):] for x in X.split()]

def main():
  N = int(sys.stdin.readline().strip())
  if N == 0:
    print('yes')
    return
  lines = list(map(foo, sys.stdin.read().splitlines()))
  uf = {}
  
  for line in lines:
    if line[0] not in uf:
      uf[line[0]] = line[0]
    if line[2] not in uf:
      uf[line[2]] = line[2]


  for line in lines:
    for word in [line[0], line[2]]:
      if word[-1] in uf:
        uf[word] = uf[word[-1]]
      elif len(word) >= 2 and word[-2:] in uf:
        uf[word] = uf[word[-2:]]
      elif len(word) >= 3 and word[-3:] in uf:
        uf[word] = uf[word[-3:]]
    a, b = uf[line[0]], uf[line[2]] 
    if (a == b) != (line[1] == 'is'):
      print('wait what?')
      return

  print('yes')

if __name__ == '__main__':
  main()
