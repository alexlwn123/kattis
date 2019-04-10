def main():
    line = list(map(int, input().split()))
    line.sort()
    a = line[-2]
    b = line[-1]
    line = line[:6]
    arr = set(i for i in range(6))
    for i in range(6):
        for j in range(1,6):
            if j == i:
                continue
            for k in range(2,6):
                if k == j or k == i:
                    continue
                first = [line[i], line[j], line[k]]
                second = []
                for v in line:
                    if v not in first:
                        second.append(v)
                if sum(first) == a and sum(second) == b:
                    if first[0] > second[0]:
                        first.extend(second)
                    else:
                        second.extend(first)
                        first = second
                    print(' '.join(list(map(str, (first[::-1])))))
                    exit()
    print(a,b)
if __name__ == '__main__':
    main()
