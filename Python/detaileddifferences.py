def main():
    n = int(input())

    for _ in range(n):
        first = input()
        second = input()
        sec = iter(second)

        out = []

        for let in list(first):
            x = next(sec)
            out.append("." if x == let else "*")
        print(first)
        print(second)
        print("".join(out))
        print("")


if __name__ == '__main__':
    main()
