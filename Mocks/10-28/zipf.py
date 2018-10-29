line = input().split(' ')
songsn, pickn = int(line[0]), int(line[1])

songs = dict()

for i in range(songsn):
    songs[tuple(input().split(' '))] = i+1

names = songs.keys()
names = sorted(names, key=lambda l: songs[l] * int(l[0]), reverse=True)
for i in range(pickn):
    print(names[i][1])
