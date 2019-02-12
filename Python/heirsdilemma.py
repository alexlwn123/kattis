def main():
    low, high = map(int, input().split())
    count = 0

    for i in range(low, high + 1):
        x = list(str(i))
        y = set(x)
        if len(x) != len(y):
            continue

        good = True

        for q in x:
            if q == '0' or i % int(q) != 0:
                good = False
                break
        if good:
            count += 1

    print(count)




if __name__ == '__main__':
    main()
