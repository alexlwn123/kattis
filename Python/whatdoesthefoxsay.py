def main():
  cases = int(input())
  for _ in range(cases):
    words = input().split(' ')
    x = set()
    y = input().split(' ')[2]
    while y != 'the':
      x.add(y)
      y = input().split(' ')[2]
    else:
      out = []
      for word in words:
        if word not in x:
          out.append(word)
      print(' '.join(out))
if __name__ == '__main__':
  main()
