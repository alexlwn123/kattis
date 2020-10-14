total = 0
def generate(nums, weight, i):
  global total

  if weight >= 200:
    return
  
  if i == len(nums):
    total -= weight
    return

  generate(nums, weight, i+1)
  generate(nums, weight+nums[i], i+1)


def main():
  N = int(input())
  nums = list(map(int, input().split()))
  global total
  for x in nums:
    total += x * 2 ** (N-1)

  generate(nums, 0, 0)

  print(total)



if __name__ == '__main__':
  main()

