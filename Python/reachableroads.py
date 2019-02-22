def find(x):
  while x != uf[x]:
    prev = x
    uf[x] = uf[uf[x]]
    x = uf[prev]
  return uf[x]

def union(x, y):
    uf[find(x)] = find(y)


def main():
    ncities = int(input())
    for _ in range(ncities):
        nends = int(input())

        global uf
        uf = [i for i in range(nends)]
        nr = int(input())

        for _ in range(nr):
            u,v = map(int, input().split())
            union(u, v)

        for i in range(len(uf)):
          find(i)

        out = len(set(uf))-1

        if out < 0:
          out = 0

        print(out)


if __name__ == '__main__':
    main()
