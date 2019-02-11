def main():
    cases = int(input())
    for _ in range(cases):
        count = int(input())
        cities = set()
        for _ in range(count):
            cities.add(input())
        print(len(cities))
if __name__ == '__main__':
    main()
