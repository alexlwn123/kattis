import sys
def main():
    line = sys.stdin.readline()
    totalmax = 1
    dp = [1] * len(line)

    for i in range(len(line)):
        maxchain = 0

        for j in range(len(line[:i])):
            if line[j] < line[i]:
                maxchain = max(maxchain, dp[j])
       
        dp[i] += maxchain
        totalmax = max(dp[i], totalmax)
    print(26 - totalmax)

if __name__ == '__main__':
    main()
