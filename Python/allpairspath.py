INFINITY = 99999999999

while True:
    n, m, q = map(int, input().split())
    if n == m == q == 0:
        break

    edges = []
    dist = [[INFINITY for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        dist[u][v] = min(w, dist[u][v])

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] >= INFINITY or dist[k][j] >= INFINITY:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[j][j] < 0 and dist[k][j] < INFINITY and dist[j][i] < INFINITY:
                    dist[k][i] = -INFINITY

    for _ in range(q):
        a, b = map(int, input().split())
        c = dist[a][b]
        if c <= -INFINITY:
            print('-Infinity')
        elif c >= INFINITY:
            print('Impossible')
        else:
            print(c)
    print('')
