def main():
    cases = int(input())
    for n in range(cases):
        print("Recipe # %d" % (n+1))
        ningr, port, dport = map(int, input().split())
        factor = dport/port

        mainweight = 0

        ingreds = {}
        for _ in range(ningr):
            line = input().split()
            ingreds[line[0]] = [float(line[1]), float(line[2])]
            if ingreds[line[0]][1] == 100:
                ingreds[line[0]][0] *= factor
                mainweight = ingreds[line[0]][0]

        for ing in ingreds:
            if ingreds[ing][1] != 100:
                ingreds[ing][0] = mainweight * ingreds[ing][1] * 0.01
            print(ing + " " + str(round(ingreds[ing][0], 1)))
        print("-" * 40)


if __name__ == '__main__':
    main()
