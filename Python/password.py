def main():
  n = int(input())
  nums = []
  for _ in range(n):
    line = input().split()
    num = float(line[1])
    nums.append(num)

  nums.sort()
  nums = nums[::-1]

  total = 0

  for i in range(len(nums)):
    total += (i+1) * nums[i]


  print(total)


if __name__ == '__main__':
  main()
