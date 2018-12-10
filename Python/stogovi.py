def main():
    n = int(input())
    stacks = [set()]

    for i in range(1, n+1):
        line = input().split(' ')
        v = int(line[1])

        stacks.append(set(stacks[v]))

        if line[0] == 'a':
           stacks[i].add(i)

        if line[0] == 'b':
            print(str(max(stacks[-1])))
            stacks[-1].remove(max(stacks[-1]))
        if line[0] == 'c':
            w = int(line[2])
            dif = stacks[v] & stacks[w]
            print(str(len(dif)))

if __name__ == '__main__':
    main()
