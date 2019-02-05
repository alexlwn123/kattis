def main():
    numMetals, numExp = map(int, input().split())
    graph = [[] for _ in range(numMetals)]
    numIn = [0 for _ in range(numMetals)]

    for _ in range(numExp):
        u, v = map(int, input().split())
        graph[u].insert(0, v)
        numIn[v] += 1

    q = []

    for i in range(numMetals):
        if numIn[i] == 0:
            q.insert(0, i)

    out = []

    for i in range(numMetals):
        if len(q) != 1:
            out = []
            break
        out.append(q[0])
        q.pop(0)

        for v in graph[out[-1]]:
            numIn[v] -= 1
            if numIn[v] == 0:
                q.insert(0, v)


    if len(out) != numMetals:
        print("back to the lab")
    else:
        print(' '.join(map(str, out)))




if __name__ == '__main__':
    main()
