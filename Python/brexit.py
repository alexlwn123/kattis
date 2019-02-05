from collections import deque
def main():
    nodes, edges, home, start = map(int, input().split())
    start -= 1
    home -= 1

    if start == home:
        print('leave')
        return

    partners = [[] for _ in range(nodes)]
    gone = [False for _ in range(nodes)]
    gonelist = [set() for _ in range(nodes)]

    for _ in range(edges):
        u,v = map(int, input().split())
        u-=1
        v-=1
        partners[u].append(v)
        partners[v].append(u)

    q = deque()

    for neighbor in partners[start]:
        gonelist[neighbor].add(start)
        q.append(neighbor)

    gone[start] = True

    while q:
        curr = q.popleft()
        if gone[curr]:
            continue

        if len(gonelist[curr]) * 2 >= len(partners[curr]):

            if curr == home:
                print('leave')
                return

            q.append(curr)
            gone[curr] = True

            for neighbor in partners[curr]:
                if gone[neighbor]:
                    continue
                gonelist[neighbor].add(curr)
                q.append(neighbor)


    print('stay')







if __name__ == "__main__":
    main()
