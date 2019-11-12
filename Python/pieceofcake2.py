n, w, h = map(int, input().split(' '))
print(max(w, n-w) * max(h, n-h)*4)
