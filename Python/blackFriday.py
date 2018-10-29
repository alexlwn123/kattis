size = int(input())
nums = input().split(' ')
nums = [int(n) for n in nums]
maxi = 0
for n in nums:
    if nums.count(n) == 1 and n > maxi:
        maxi = n
if maxi != 0: print(str(nums.index(maxi)+1))
else: print('none')
