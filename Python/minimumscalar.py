def main():

    cases = int(input())

    for i in range(cases):
        size = int(input())
        x = input().split(' ')
        y = input().split(' ')
        x = map(lambda i: int(i), x)
        y = map(lambda i: int(i), y)
        x = sorted(x)
        y = sorted(y, reverse=True)
        out = sum([int(x[j]) * int(y[j]) for j in range(size)])
        print("Case #" + str(i + 1) + ": " + str(out))


if __name__ == '__main__':
    main()
