
def main():
    n = int(input())
    trips = {}
    for _ in range(n):
        line = input().split(' ')
        p, d = line[0], int(line[1])
        if p in trips:
            trips[p].append(d)
        else:
            trips[p] = [d]

    for k in trips:
        trips[k].sort()

    q = int(input())
    for _ in range(q):
        line = input().split(' ')
        p, t = line[0], int(line[1])-1
        print(trips[p][t])

if __name__ == '__main__':
    main()
