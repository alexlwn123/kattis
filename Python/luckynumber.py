count = 0
def generate(num, k, MAX):
  global count
  if num % k != 0:
    return
  if k == MAX:
    count += 1
    return

  for i in range(10):
    nex = num * 10 + i
    generate(nex, k+1, MAX)


def main():
  N = int(input())
  global count
  for i in range(1, 10):
    generate(i, 1, N)

  print(count)


if __name__ == '__main__':
  main()
