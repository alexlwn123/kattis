import sys
def main():
  for line in sys.stdin.read().splitlines():
    out = set()
    reverse = line[::-1]
    for i in range(2, len(line)+1):
      j = 0
      while i + j < len(line)+1:
        if j != 0 and line[j:i+j] == reverse[-(i + j):-j]:
          out.add(line[j:i+j])
        elif j == 0 and line[:i] == reverse[-i:]:
          out.add(line[:i])
        j += 1
    print('\n'.join(sorted(out)))
    print()



if __name__ == '__main__':
  main()
