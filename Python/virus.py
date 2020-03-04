import sys
A, B = sys.stdin.read().splitlines()
i, j, c = 0, 0, 0

while i < len(A) and i < len(B) and A[i] == B[i]:
  i += 1
j = -1
z = min(len(A), len(B))
while (z-i-(-j-1)) > 0 and j >= -len(A) and j >= -len(B) and A[j] == B[j]:
  j-=1

print(len(B)-(i-j-1))
    
  

