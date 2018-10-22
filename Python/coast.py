import sys

def main():
    lines = sys.stdin.read().splitlines();
    line1 = lines[0].split(" ")
    height = line1[0]
    width = line1[1]
    lines = lines[1:]



    for i in range(height):
        for j in range(width):



    lines = unionFind(lines)




class node:

    def __init__(self, land = None, xy = None):
        self.xy = xy
        self.land = land
        self.neighbors = []
        self.visited = false

    def doDFS():

if __name_ == '__main__':
    main()
