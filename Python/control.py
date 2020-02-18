import sys
def find(arr, n):
  if arr[n] == n:
    return n
  arr[n] = find(arr, arr[n])
  return arr[n]

def union (arr, size, u, v):
  ur, vr = find(arr, u), find(arr, v)
  if ur == vr:
    return

  if size[ur] >= size[vr]:
    size[ur] += size[vr]
    arr[vr] = ur
  else:
    size[vr] += size[ur]
    arr[ur] = vr

def main():
  lines = sys.stdin.read().splitlines()
  N = int(lines[0])
  arr, size = [i for i in range(500001)], [1] * 500001
  out = 0

  for line in lines[1:]:
    X = list(map(int, line.split()))
    left = {} 
    for x in X[1:]:
      xr = find(arr, x)
      if xr not in left:
        left[xr] = size[xr]-1
      else:
        left[xr] -= 1

    if sum(left.values()) == 0:
      out += 1
      for x in X[2:]:
        union(arr, size, X[1], x)

  print(out)
  

if __name__ == '__main__':
  main()
