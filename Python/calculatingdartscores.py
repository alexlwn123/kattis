def main():
  n = int(input())
  dic = {1: 'single', 2: 'double', 3:'triple'}
  for a in range(4):
    for b in range(4):
      for c in range(4):
        for i in range(1,21):
          for j in range(1,21):
            for k in range(1,21):
              if a*i + b*j + c*k == n:
                if a!=0:
                  print(dic[a], i)
                if b!=0:
                  print(dic[b], j)
                if c!=0:
                  print(dic[c], k)
                return

  print('impossible')

if __name__ == '__main__':
  main()
