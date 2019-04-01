def main():
  n = int(input())
  while n:
    bits = [-1 for i in range(32)]
    for i in range(n):
      line = input().split()

      if line[0] == 'SET':
        bits[int(line[1])] = 1
      elif line[0] == 'CLEAR':
        bits[int(line[1])] = 0
      elif line[0] == 'AND':
        i, j = int(line[1]), int(line[2])
        if bits[i] == 0 or bits[j] == 0:
          bits[i] = 0
        elif bits[i] == 1 and bits[j] == 1:
          bits[i] = 1
        else:
          bits[i] = -1
      elif line[0] == 'OR':
        i, j = int(line[1]), int(line[2])
        if bits[i] == 1 or bits[j] == 1:
          bits[i] = 1
        elif bits[i] == -1 or bits[j] == -1:
          bits[i] = -1
    n = int(input())

    for i in range(32):
      if bits[i] == -1:
        bits[i] = "?"
      else:
        bits[i] = str(bits[i])

    print("".join(bits[::-1]))
if __name__ == '__main__':
  main()
