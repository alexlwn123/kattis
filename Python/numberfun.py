def main():
  n = int(input())
  for _ in range(n):
    x, y, z = map(int, input().split())
    if x+y == z or x-y == z or x*y == z or (y!=0 and x%y==0 and x//y==z) or y-x == z or (x!=0 and y%x == 0 and y//x==z):
      print('Possible')
      continue
    print('Impossible')

if __name__ == '__main__':
  main()
