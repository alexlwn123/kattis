def main():
  n = int(input())
  arr = list(int, input().split())
  arr = arr[::-1]
  count = 0
  for i in range(n-1):
    if arr[i] < arr[i+1]:
      count += arr[i+1] - arr[i]

if __name__ == '__main__':
  main()
