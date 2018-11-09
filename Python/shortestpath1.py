#Fastest time on Kattis for Python3

import sys
from heapq import heappush, heappop
from collections import defaultdict
def main():

    line = sys.stdin.readline().strip()
    while True:
        line = list(map(int, line.split(' ')))

        n, m, q, start = line

        adj = defaultdict(list)
        distances = {}

        for _ in range(m):

            line = sys.stdin.readline().strip().split()
            u, v, w = list(map(int, line))

            adj[u].append((v, w))


        queue = [(0, start)]
        heappush(queue, (0, start))


        while len(distances) < n and queue:

            cost, current  = heappop(queue)
            if current in distances and distances[current] <= cost:
                continue

            distances[current] = cost
            for neighbor, val in adj[current]:
                if neighbor in distances and distances[neighbor] <= cost+val:
                    continue
                heappush(queue, (cost + val, neighbor))

        for __ in range(q):
            dest = int(sys.stdin.readline().strip())
            if dest not in distances:
                print('Impossible')
                continue

            print(str(distances[dest]))

        line = sys.stdin.readline().strip()

        if line == '0 0 0 0':
          break

        print


if __name__ == '__main__':
    main()
