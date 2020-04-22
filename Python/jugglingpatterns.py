import sys
from heapq import heappush, heappop, heapify
def main():
  for line in sys.stdin.read().splitlines():
    nums = list(map(int, list(line)))
    if sum(nums) % len(nums) != 0:
      print(f"{line}: invalid # of balls")
      continue

    i = 0
    left, right = [], []
    s = []
    l = True
    for n in nums:
      if l == (n%2==0):
        s.append(i+n)
        heappush(left, i+n)
      else:
        s.append(i+n)
        heappush(right, i+n)
      i+=1
    if len(s) == len(set(s)) and len(left) == len(set(left)) and len(right) == len(set(right)):
      print(f'{line}: valid with {sum(nums)//len(nums)} balls')
    else:
      print(f'{line}: invalid pattern')




      






if __name__ == '__main__':
  main()
