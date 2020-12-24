def main():
  m, n = map(int, input().split())
  curr = 0 
  count = 0
  for _ in range(n):
    line = input().split()
    if line[0] == 'enter':
      if curr + int(line[1]) > m:
        count += 1
      else:
        curr += int(line[1])

    else:
      curr -= int(line[1])

  print(count)



  


if __name__ == '__main__':
  main()
