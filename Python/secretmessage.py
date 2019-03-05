def main():
  n = int(input())
  for _ in range(n):
    line = input()
    x = len(line)
    size = find(x)

    arr = []
    for i in range(size):
      arr.append(['*' for i in range(size)])
    line = iter(line)
    try:
      for i in range(size * size):
        arr[i // size][i % size] = next(line)
    except StopIteration as Exception:
      pass
    out = []
    for i in range(size):
      for j in range(size-1, -1, -1):
        out.append(arr[j][i])
    for i in range(len(out)-1):
      if out[i] == '*':
        del out[i]
    print("".join(out))

def find(n):
  i = 1
  while True:
    if i * i >= n:
      return i
    i += 1

if __name__ == '__main__':
  main()
