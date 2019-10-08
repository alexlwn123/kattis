def main():
  n = int(input())
  arr = list(map(int, input().split()))[::-1]
  count = 0
  for i in range(1, n):
    if arr[i] >= arr[i-1]:
      count += arr[i] - arr[i-1] + 1
      arr[i] = arr[i-1] - 1
  if arr[-1] < 0:
    count = 1
  print(count)
if __name__ == '__main__':
  main()
