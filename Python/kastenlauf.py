def main():
    cases = int(input())
    while cases:
        nstores = int(input())
        x0,y0 = map(int, input().split())

        stores = [(x0,y0)]
        for _ in range(nstores):
            x,y = map(int, input().split())
            stores.append((x,y))

        x1,y1 = map(int, input().split())

        isGood = {i:False for i in range(len(stores))}

        edges = []

        for i in range(len(stores)):
            for j in range(len(stores)):
                if x1 == x0 and y1 == y0:
                    continue
                dist = abs(x1-x0) + abs(y1-y0)


        cases -= 1
if __name__ == '__main__':
    main()
