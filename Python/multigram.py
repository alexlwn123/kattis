def main():
  line = input()
  asci = [int(ord(c)) for c in line]
  for i in range(1, len(line)//2+1):
    if len(line) % i != 0:
      continue
    sub = sum(asci[:i])
    for j in range(len(line)//i):

      if sum(asci[j*i:(j+1)*i]) != sub:
        break
    else:
      print(line[:i])
      return

  print(-1)



if __name__ == '__main__':
  main()
