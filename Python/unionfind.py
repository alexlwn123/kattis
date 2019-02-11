from sys import stdin, stdout
def find(elem):

    if elem == arr[elem]:
        return arr[elem]

    arr[elem] = find(arr[elem])
    return arr[elem]

def union(u, v):

    u1, v1 = find(u), find(v)

    if u1 == v1:
       return
    if rank[u1] < rank[v1]:
        arr[u1] = v1
    elif rank[v1] < rank[u1]:
        arr[v1] = u1
    else:
        arr[v1] = u1
        rank[u1] += 1


def main():
    elems, queries = map(int, stdin.readline().split(' '))
    global arr, rank
    arr = [i for i in xrange(elems+1)]
    rank = [0] * (elems+1)
    out = []

    try:
        while True:

            line = stdin.readline().split()
            u,v = map(int, line[1:])

            if line[0] == '=':
                union(u, v)

            else:
                out.append('yes' if find(u) == find(v) else 'no')

    except ValueError as Exception:
        stdout.write("\n".join(out))
if __name__ == '__main__':
    main()
