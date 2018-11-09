import sys
def main():
    inf = 9999
    n = int(sys.stdin.readline())
    adj = dict()
    for _ in range(n):
        line = sys.stdin.readline().strip().split(' ')
        for word in line[1:]:
            if line[0] in adj:
                adj[line[0]].add(word)
            else:
                adj[line[0]] = {word}
            if word in adj:
                adj[word].add(line[0])
            else:
                adj[word] = {line[0]}

    start, dest = (sys.stdin.readline().split())

    distances = {stop: inf for stop in adj}
    distances[start] = 0

    prev = dict()

    verticies = adj.copy()

    while verticies:

        current = min(verticies, key=lambda x: (distances[x]))

        if distances[current] == inf:
            print('no route found')
            exit()

        for neighbor in adj[current]:
            route = distances[current] + 1

            if route < distances[neighbor]:
                distances[neighbor] = route
                prev[neighbor] = current

        del verticies[current]

    path, current = [], dest

    while current in prev:
        path.insert(0, current)
        current = prev[current]

    if path:
        path.insert(0, current)

    print(str(' '.join(path)))




if __name__ == '__main__':
    main()
