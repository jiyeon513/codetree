n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

OFFSET = 100000
SIZE = 200001

white = [0] * SIZE
black = [0] * SIZE
color = [''] * SIZE
gray = [False] * SIZE

loc = 0

for a in range(n):

    if dir[a] == 'R':
        for i in range(x[a]):
            idx = loc + i + OFFSET

            if not gray[idx]:
                black[idx] += 1
                color[idx] = 'B'

                if black[idx] >= 2 and white[idx] >= 2:
                    gray[idx] = True

        loc += x[a] - 1

    else:  # L
        for i in range(x[a]):
            idx = loc - i + OFFSET

            if not gray[idx]:
                white[idx] += 1
                color[idx] = 'W'

                if black[idx] >= 2 and white[idx] >= 2:
                    gray[idx] = True

        loc -= x[a] - 1

w = b = g = 0

for i in range(SIZE):
    if gray[i]:
        g += 1
    elif color[i] == 'W':
        w += 1
    elif color[i] == 'B':
        b += 1

print(w, b, g)