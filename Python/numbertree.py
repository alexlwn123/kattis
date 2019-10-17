def main():
  line = input().split(' ')

  h = int(line[0]) + 1
  n = sum([2 ** i for i in range(h)])
  if len(line) == 1:
    print(n)
    return

  word = line[1]
  layer = len(word)
  curr = 1
  for i in range(h-1, layer, -1):
    curr += 2 ** i
  layer -= 1
  for let in word:
    if let == 'R':
      layer -= 1
    else:
      curr += 2 ** layer
      layer -= 1

  print(curr)

if __name__ == '__main__':
  main()
