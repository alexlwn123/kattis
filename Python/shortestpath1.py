import sys
from heapq import heappush, heappop
from collections import defaultdict, deque
def main():
    lines, out = iter(sys.stdin.readlines()), deque()
    x = next(lines)
    while x != '0 0 0 0':
        n, m, q, start = map(int, x.split(' '))

        adj = defaultdict(list)
        distances = {}

        for _ in range(m):

            u, v, w = map(int, next(lines).split())
            adj[u].append((v, w))

        queue = [(0, start)]

        while len(distances) < n and queue:

            cost, current = heappop(queue)
            if current in distances and distances[current] <= cost:
                continue

            distances[current] = cost
            for neighbor, val in adj[current]:
                if neighbor in distances and distances[neighbor] <= cost+val:
                    continue
                heappush(queue, (cost + val, neighbor))

        for _ in range(q):
            dest = int(next(lines))
            if dest in distances:
                out.append(str(distances[dest]))
                continue

            out.append('Impossible')

        out.append("")
        x = next(lines)
    print('\n'.join(out))

if __name__ == '__main__':
    main()
