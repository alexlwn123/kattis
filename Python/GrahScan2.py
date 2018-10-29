def main():
    line = input()
    while line != '0':
        size = int(line)
        points = []

        for i in range(size):
            line = input().split(' ')
            p = Point(int(line[0]), int(line[1]))
            if not p in points:
                points.append(p)

        out = gScan(points)

        print(len(out))

        #for point in out:
            #print(point)
        print('\n'.join(str(p) for p in out))

        line = input()

def gScan(points):

    def slope(p1, p2):
        if p1.x == p2.x:
            return float('inf')
        return 1.0 * (p2.y - p1.y) / (p2.x - p1.x)

    def cross(p1, p2, p3):
        return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)


    start = min(points, key=lambda p: (p.x,p.y))
    points.pop(points.index(start))

    points.sort(key=lambda p: (slope(start, p), -p.y, p.x))

    ans = [start]
    for p in points:
        ans.append(p)
        while len(ans) > 2 and cross(ans[-3], ans[-2], ans[-1]) < 0:
            ans.pop(-2)

    return ans


class Point:

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

if __name__ == '__main__':
    main()
