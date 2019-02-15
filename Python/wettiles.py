from collections import deque
def main():
    WALL = -9999
    directions = [[0,1], [1,0], [-1,0], [0,-1]]
    while True:
        line = input()
        if line == '-1':
            break
        width, height, time, numleaks, numwalls = map(int, line.split())
        leaks = []
        graph = [[0 for x in range(height)] for i in range(width)]
        numleaks *= 2

        while numleaks:
            line = list(map(int, input().split()))
            line = [x-1 for x in line]
            numleaks -= len(line)
            leaks.extend(line)

        leaks = zip(leaks[0::2], leaks[1::2])
        numwalls *= 4
        walls =[]
        while numwalls:
            line = list(map(int, input().split()))
            line = [x-1 for x in line]
            numwalls -= len(line)
            walls.extend(line)

        walls = list(zip(walls[0::2], walls[1::2]))
        for i in range(len(walls) // 2):
            x0, y0 = walls[i*2]
            x1, y1 = walls[i*2 + 1]
            dx,dy = x1-x0, y1-y0

            if dx == dy == 0:
                graph[x0][y0] = WALL
                continue

            if dx != 0:
                dx //= abs(dx)
            if dy != 0:
                dy //= abs(dy)

            x, y = x0,y0

            while x != x1+dx or y != y1+dy:
                graph[x][y] = WALL
                x, y = x+dx, y+dy

        q = deque()
        count = 0

        for leak in leaks:
            x,y = leak
            if graph[x][y] == 0:
                q.append((x,y))
                graph[x][y] = 1
                count += 1

        while q:
            x0,y0 = q.popleft()

            if graph[x0][y0] == time:
                continue

            for dx,dy in directions:
                x,y = x0+dx, y0+dy
                if x < 0 or x >= width or y < 0 or y >= height:
                    continue

                if graph[x][y] > graph[x0][y0]+1:
                    graph[x][y] = graph[x0][y0]+1
                    q.append((x,y))
                    continue

                elif graph[x][y] != 0:
                    continue

                graph[x][y] = graph[x0][y0] + 1
                count+=1
                if graph[x][y] < time:

                    q.append((x,y))

        print(count)
if __name__ == '__main__':
    main()
