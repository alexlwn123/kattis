def main():
  H,W,N,M = map(int,input().split())
  before = [list(map(int,input().split())) for _ in range(H)]
  ker = [list(map(int,input().split()))[::-1] for _ in range(N)][::-1]
  image = [[0]*(W-M+1) for _ in range(H-N+1)]
  for i in range(len(image)):
    for j in range(len(image[i])):
      for a in range(len(ker)):
        for b in range(len(ker[a])):
          image[i][j] += before[i+a][j+b] * ker[a][b]

  print('\n'.join([' '.join(list(map(str, arr))) for arr in image]))







if __name__ == '__main__':
  main()
