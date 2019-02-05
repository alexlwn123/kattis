from collections import OrderedDict
def main():
    case = 0
    n = int(input())

    while n != 0:

        animals = {}
        case += 1
        for _ in range(n):
            line = input().split()
            animal = line[-1].lower()
            if animal in animals:
                animals[animal] += 1
            else:
                animals[animal] = 1

        alphabetical = OrderedDict(sorted(animals.items()))
        print("List %d:" % case)
        for animal in alphabetical:
            print("{} | {}".format(animal, alphabetical[animal]))
        n = int(input())


if __name__ == '__main__':
    main()
