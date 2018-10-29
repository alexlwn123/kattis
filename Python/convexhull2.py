def main():
    size = int(input())
    points = []

    for i in range(size):
        line = input().split(' ')
        if line[2] == 'Y':
            p = (int(line[0]), int(line[1]))
            points.append(p)
    start = min(points, key=lambda p: (p[0], p[1]))
    points.pop(points.index(start))

    points = sorted(points, key=lambda p: (slope(start, p), p[0], p[1]))

    points.insert(0, start)
    out = '\n'.join(str(point[0]) + " " + str(point[1]) for point in points)

    if len(points) > 1:
        points = gScan(points)
    print(len(points))
    print(out)

def gScan(points):

    def cross(p1, p2, p3):
        return (p2[0]- p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])


    start = min(points, key=lambda p: (p[0],p[1]))

    points.pop(points.index(start))

    points.sort(key=lambda p: (slope(start, p), -p[1], p[0]))

    ans = [start]
    for p in points:
        ans.append(p)
        while len(ans) > 2 and cross(ans[-3], ans[-2], ans[-1]) < 0:
            ans.pop(-2)

    return ans


def slope(p1, p2):
    if p1[0] == p2[0]:
        return float('inf')
    return 1.0 * (p2[1] - p1[1]) / (p2[0] - p1[0])
"""
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return str(self.x) + " " + str(self.y)
"""
if __name__ == '__main__':
    main()


