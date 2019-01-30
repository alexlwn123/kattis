import string
def main():
    while True:
        line = raw_input()
        n,m,q,s = map(int, line.split(' '))

        if n == m == q == s == 0:
            break
        edges = []


        for i in range(m):

            u,v,w = map(int, raw_input().split())
            edges.append([u,v,w])

        #BellmanFord:
        dist = [float("Inf") for _ in xrange(n)]
        dist[s] = 0

        for i in range(n-1):

            for u,v,w in edges:
                if dist[u] == float("Inf"):
                    continue
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        while True:
            nchanged = 0
            for u,v,w in edges:
                if dist[v] == -float("Inf") or dist[u] == float("Inf"):
                    continue
                if dist[u] + w < dist[v]:
                    dist[v] = -float("Inf")
                    nchanged += 1
            if nchanged == 0:
                break


        #queries and output

        for _ in xrange(q):
            end = int(raw_input())
            out = dist[end]
            print("-Infinity" if out <= -float("Inf") else ("Impossible" if out >= float("Inf") else out))
        print
if __name__ == '__main__':
    main()
