import sys
def main():
  lines = sys.stdin.readlines()
  while lines:
    width = len(lines[0])
    height = 0
    for line in lines:
      if len(line) != width:
        break
      height += 1


if __name__ == '__main__':
  main()
