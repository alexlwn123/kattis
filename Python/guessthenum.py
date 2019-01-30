from itertools import permutations
import re
import time
def main():
    memo = [dict() for i in range(1001)]
    count = 0
    s = time.time()
    out = []
    line = input().split(' ')
    p = re.compile('[a-z]')

    while line != ['0', '0']:
        count += 1
        n = int(line[0])
        nums = line[1:-1]
        target = int(line[-1])
        line = input()
        line = p.sub('{}', line)

        if line in memo[target] and nums in memo[target][line]:
            out.append('NO')
            line = input().split(' ')
            continue

        perms = permutations(nums)
        done = False

        for perm in perms:
            if eval(line.format(*perm)) == target:
                out.append('YES')
                done = True
                break

        if not done:
            out.append('NO')
            if line not in memo[target]: memo[target][line] = []
            memo[target][line].append(nums)

        line = input().split(' ')

    print('\n'.join(out))
    print('time' + str(time.time()-s) + ' count: ' + str(count))
    print(str(memo[89]))
    print(str(memo[1]))
if __name__ == '__main__':
    main()
