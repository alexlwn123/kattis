import sys
def main():
  lines = sys.stdin.read().splitlines()

  N, Q = map(int, lines.pop(0).split())

  people = {}

  start = '0'  
  out = []


  for line in lines:
    arr = line.split()
    if arr[0] == 'SET':
      people[arr[1]] = arr[2]
    elif arr[0] == 'RESTART':
      del people
      people = {}
      start = arr[1]
    else:
      if arr[1] in people:
        out.append(people[arr[1]])
      else:
        out.append(start)


  sys.stdout.write("\n".join(out))




if __name__ == '__main__':
  main()
