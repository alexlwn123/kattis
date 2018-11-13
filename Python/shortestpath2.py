import sys
from collections import defaultdict
from heapq import heappush, heappop

def main():
    n, m, q, s = list(map(int, sys.stdin.readline().strip().split()))

    while not (n == m == s == q == 0):

        adj = defaultdict(list)
        distances = {}

        for _ in range(m):
            u, v, t, p, d = list(map(int, sys.stdin.readline().strip().split()))
            adj[u].append((v, d, t, p))

        queue = [(0, s)]
        heappush(queue, (0, s))

        while len(distances) < n and queue:

            cost, current = heappop(queue)

            if current in distances and distances[current] <= cost:
                continue

            distances[current] = cost

            for neighbor, d, t, p in adj[current]:
                if cost <= t:
                    val = d + t
                elif p != 0:
                    val = (p - (cost - t) % p) % p + d + cost
                else:
                    continue

                if neighbor in distances and distances[neighbor] <= val:
                    continue
                heappush(queue, (val, neighbor))

        for _ in range(q):
            dest = int(sys.stdin.readline().strip())
            if dest not in distances:
                print('Impossible')
                continue
            print(str(distances[dest]))

        n, m, q, s = list(map(int, sys.stdin.readline().strip().split()))

        if not n == m == q == s == 0:
            print



if __name__ == '__main__':
    main()
