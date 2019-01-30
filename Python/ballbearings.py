import math
def main():
    cases = int(input())
    for i in range(cases):
        big, small, space = map(float, input().split())

        radius = (big-small) / 2
        angle = math.acos((-((small + space) ** 2) + 2 * radius ** 2) / (2 * radius ** 2))



        print("%d" % int(2 * math.pi / angle))

if __name__ == '__main__':
    main()
