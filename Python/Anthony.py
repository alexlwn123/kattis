import sys
import math
def main():

    nums = sys.stdin.readline().split(' ')
    if math.sqrt(float(nums[0]) / math.pi) <= float(nums[1]) / (2 * math.pi):
        print('Diablo is happy!')
    else:
        print('Need more materials!')
       



if __name__ == '__main__':
    main()
