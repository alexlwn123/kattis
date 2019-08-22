def main():
  x, y = list(map(int, input().split()))
  for x in range(min(x,y)+1, max(x,y)+2):
    print(x)
if __name__ == '__main__':
  main()
