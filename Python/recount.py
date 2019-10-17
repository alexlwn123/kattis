import sys
def main():
  names = {}
  lines = sys.stdin.readlines()
  del lines[-1]
  for line in lines:
    line = line.strip()
    if line in names:
      names[line] += 1
    else:
      names[line] = 1
    line = sys.stdin.readline()

  names, values = list(names.keys()), list(names.values())

  big = max(values)

  if values.count(big) != 1:
    print('Runoff!')
  else:
    print(names[values.index(big)])

if __name__ == '__main__':
  main()
