arr = [sum(map(int, input().split())) for _ in range(5)]
tmax = 1
imax = 0

for i in range(5):
  if arr[i] > imax:
    tmax = i + 1
    imax = arr[i]
print(tmax, imax)
