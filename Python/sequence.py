import sys
import math
def main():
    n = int(sys.stdin.readline())
    start = int(math.sqrt(n))
    nums = []

    for i in range(start, 2, -1):
        if n % i == 0:
            n %= i
            nums.insert(0,i)
    if n != 1:
        nums.insert(0,n)
    nums.insert(0,1)

    print(str(len(nums)))
    out = str(nums[0])
    for val in nums[1:]:
        out += ' ' + str(val)

    print(out)

if __name__ == '__main__':
    main()
