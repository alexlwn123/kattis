jack = [0 for x in range(1000001)]
while True:
    n, m = (int(x) for x in raw_input().split())
    if n == 0 and m == 0:
        break
    i = 0
    for _ in xrange(n):
        jack[i] = int(raw_input())
        i += 1
    i, c = 0, 0
    for _ in xrange(m):
        a = int(raw_input())
        while i < n and jack[i] < a:
            i += 1
        if i < n and jack[i] == a:
            c += 1
    print c
