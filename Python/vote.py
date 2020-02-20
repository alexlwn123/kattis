import sys
def main():
  n = int(sys.stdin.readline().strip())
  for _ in range(n):
    N = int(sys.stdin.readline().strip())
    arr = []
    for _ in range(N):
      arr.append(int(sys.stdin.readline().strip()))
    m = max(arr)
    s = sum(arr)
    if arr.count(m) != 1:
      print('no winner')
    elif m*2 > sum(arr):
      print('majority winner', arr.index(m)+1)
    else:
      print('minority winner', arr.index(m)+1)


      
      


if __name__ == '__main__':
  main()
