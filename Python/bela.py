def main():
  N,B = input().split()
  norm = {"A": 11, "K": 4, "Q":3, "J":2, "T": 10, "9": 0, "8": 0, "7": 0}
  dom = {"A": 11, "K": 4, "Q":3, "J":20, "T": 10, "9": 14, "8": 0, "7": 0}
  total = 0
  for _ in range(4*int(N)):
    line = input()
    if line[1] == B:
      total += dom[line[0]]
    else:
      total += norm[line[0]]

  print(total)




if __name__ == '__main__':
  main()    
