import sys
import functools
def main():
    lines = int(input().strip())
    while lines != 0:
        files = {}
        for _ in range(lines):
            line = input()

            single = functools.reduce(lambda a,b : a ^ b, list(map(ord,line)))
            if single not in files:
                files[single] = [0,{}]
            files[single][0] += 1
            if line not in files[single][1]:
                files[single][1][line] = 1
            else:
                files[single][1][line] += 1

        collisions = 0
        uniques = 0
        for _, val in files.items():
            if val[0] > 1:
                for k,v in val[1].items():
                    collisions += (val[0] - v) * v
                uniques += len(val[1])
            else:
                uniques += 1

        print("%d %d" % (uniques, collisions//2))
        lines = int(input().strip())

if __name__ == '__main__':
    main()
