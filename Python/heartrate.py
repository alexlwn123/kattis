def main():
  n = int(input())
  for _ in range(n):
    line = input().split(' ')
    b, p = int(line[0]), float(line[1])

    BPM = 60 * b / p
    LBPM = 60 * (b-1) / p
    HBPM = 60 * (b+1) / p


    print(LBPM, BPM, HBPM)



if __name__ == '__main__':
  main()
