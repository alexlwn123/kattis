dp = [0, 2, 3, 5]
n = int(input())


for i in range(3, 10005):
  dp.append(dp[i-1] + dp[i])

for _ in range(n):
  print(dp[int(input())] % (10 ** 9 + 7))

