from collections import defaultdict
def main():
  word = input()
  N = int(input())
  nexts = defaultdict(list)
  for _ in range(N):
    x = input()
    nexts[x[0]].append(x)

  if not nexts[word[-1]]:
    print('?')
    return

  for nex in nexts[word[-1]]:
    if len(nexts[nex[-1]]) == 0 or (len(nexts[nex[-1]]) == 1 and nex[-1] == nex[0]):
      print(nex, '!', sep='')
      return

  print(nexts[word[-1]][0])
  return





if __name__ == '__main__':
  main()
