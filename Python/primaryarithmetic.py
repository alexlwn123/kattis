def main():
    while True:
      x, y = [0] * 10, [0] * 10

      a, b = map(list, input().split())
      a, b = list(map(int,a)), list(map(int,b))

      a = a[::-1]
      b = b[::-1]
      if a == b == [0]:
        break
      for i in range(len(a)):
        x[i] = a[i]
      for i in range(len(b)):
        y[i] = b[i]
      count = 0
      carry = 0
      for i in range(10):
        curr = x[i] + y[i] + carry
        if curr >= 10:
          count += 1
        carry = curr / 10
      if count == 0:
        print('No carry operation.')
      elif count == 1:
        print('1 carry operation.')
      else:
        print(count, 'carry operations.')


if __name__ == '__main__':
  main()
