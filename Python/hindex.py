def main():
    n = int(input())
    citations = []
    for i in range(n):
        citations.append(int(input()))

    counts = [0] * (n + 1)

    for i in range(n):
        x = citations[i]
        if x >= n:
            counts[n] += 1
        else:
            counts[x] += 1

    out = 0

    for i in range(n, -1, -1):
        out += counts[i]
        if out >= i:
            print(str(i))
            exit()

    print(str(out))

if __name__ == '__main__':
    main()
