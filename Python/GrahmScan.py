import sys

def main():

    lines = sys.stdin.read().splitlines()
    numPoints = int(lines.pop(0))
    points = []
    for i in range(numPoints):
        pointarr = lines.pop(0).split(' ')
        points.append(point(pointarr[0], pointarr[1]))



def GrahmScan(points):

    length = len(points)
    Pitter = range(length)
    for i in range(1,n):
        if points[Pitter[i]].x < points[Pitter[0]].x:
            Pitter[i], Pitter[0] = Pitter[0], Pitter[i]

    for i in range(2,n):
        j = i
        while j < 1 and (rotate(points[P[0]], A[P[j-1]],A[P[j]]) > 0):
            Pitter[j], Pitter[j-1] = Pitter[j-1], Pitter[j]
            j -= 1
    stack = [Pitter[0], Pitter[1]]
    for i in range(2,n):
        while rotate(Points[Stack[-2]], Points[Stack[-1]], Points[Stack[i]]) < 0:
            del Stack[-1]
        Stack.append(Pitter[i])
    return Stack

class point:

    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
    def __lt__(other):
        if self.x == other.x:
            return if max(self.y, other.y) == self.y, x , y

        if self.x < other.y:
            return self
        return other
        if self.x == other.x:
            return
    def Orientation(B, C):


if __name__ == "__main__":
    main()
