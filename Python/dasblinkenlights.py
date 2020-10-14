from math import gcd
p,q,s = map(int, input().split())
ans = 'no'
if p * q // gcd(p, q) <= s:
  ans = 'yes'
print(ans)
