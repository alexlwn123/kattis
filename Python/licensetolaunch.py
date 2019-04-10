def main():
  n = int(input())
  nums = list(map(int, input().split()))
  x = min(nums)
  print(nums.index(x))
if __name__ == '__main__':
  main()
