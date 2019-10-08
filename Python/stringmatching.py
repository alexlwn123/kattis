import sys, re
def main():
  lines = sys.stdin.readlines()
  out = []
  for i in range(0, len(lines), 2):
    pattern, line = lines[i].strip(), lines[i+1].strip()
    start = 0

    while True:
      start = line.find(pattern, start)
      if start == -1:
        return

    out.append(' '.join(finds))

  print('\n'.join(out))

# if __name__ == '__main__':
#   main()

# import sys
# def main():
#   lines = sys.stdin.readlines()
#   out = []
#   for i in range(0, len(lines), 2):
#     p, w = lines[i].strip(), lines[i+1].strip()
#     arr = []
#     i, j = 0,0
#     while w.find(p):
#       arr.append

#   print(lines)
# if __name__ == '__main__':
#   main()
