import math
x, y = map(float, input().split(' '))

area = ((y / math.pi) / 2) ** 2 * math.pi

print('Need more materials!' if area < x else 'Diablo is happy!')
