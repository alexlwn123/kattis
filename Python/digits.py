from sys import stdin
def find(string):
  if len(str(string)) == 1:
    return 2
  return 1 + find(str(len(string)))


def main():
  lines = stdin.readlines()[:-1]
  out = []
  for line in lines:
    x = line.strip()
    if x == '1':
      out.append('1')
    else:
      out.append(str(find(x)))
  print('\n'.join(out))
if __name__ == '__main__':
  main()
