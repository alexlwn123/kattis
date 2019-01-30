def main():
    n = int(input())
    while n != 0:
        foods = dict()
        for i in range(n):
            line = input().split()
            for food in line[1:]:
                if food not in foods:
                    foods[food] = set()
                foods[food].add(line[0])

        for food in sorted(foods):
            print(food + " " + " ".join(sorted(foods[food])))
        print()
        n = int(input())

if __name__ == '__main__':
    main()
