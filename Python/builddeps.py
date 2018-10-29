length = int(input())
nodes = dict()
for i in range(length):
    line = input().split(' ')
    name = line[0][:-1]
    line = line[1:]
    nodes[name] = []
    while len(line) > 0:
        if line[0] in nodes:
            nodes[line[0]].append(name)
            line = line[1:]
        else:
            nodes[line[0]] = []

top = input()
queue = [top]
visited = [top]
while len(queue) > 0:
    print(queue[0])
    visited.append(queue[0])
    currentlen = len(queue)
    for child in nodes[queue[0]]:
        if child not in visited:
            place = len(queue)
            for item in subq:
                if item in nodes[child]:
                   subq[0], subq[-1] = subq[-1], subq[0]

            visited.append(child)
            queue.append(child)
    queue = queue[1:]







