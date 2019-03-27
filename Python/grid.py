import sys
from heapq import heappush as push,heappop as pop

def travel(graph,n,m):
    dis = [-1 for i in xrange(n*m)]
    q = []
    target = n*m-1
    push(q,(0,0))
    dis[0] = 0
    while(len(q)>0):
        d,v = pop(q)
        for u in graph[v]:
            if dis[u] == -1 or (dis[u] > d+1):
                dis[u] = d+1
                if u == target:
                    return d+1
                push(q,(dis[u],u))
    return dis[-1]

def make_graph(data,rows,cols):
    graph = {}
    for x in xrange(rows):
        for y in xrange(cols):
            val = int(data[x][y])
            i_d = x*cols+y
            graph[i_d] = []
            if (x + val) < rows:
                graph[i_d].append((x+val)*cols + y)
            if (x - val) >= 0:
                graph[i_d].append((x-val)*cols + y)
            if (y + val) < cols:
                graph[i_d].append((x*cols)+ y + val)
            if (y - val) >= 0:
                graph[i_d].append((x*cols)+ y - val)
    return graph


def main():
    rows,cols = [int(n) for n in sys.stdin.readline().split()]
    data = []
    for i in xrange(rows):
        data.append(sys.stdin.readline().strip())

    graph = make_graph(data,rows,cols)
    print travel(graph,rows,cols) # uses Dijkstra's Algorithm

if __name__ == '__main__':
    main()

