n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

diff = [0] * 201

for a, b in segments:
    diff[a + 100] += 1
    diff[b + 100] -= 1

arr = [0] * 200
arr[0] = diff[0]

for i in range(1, 200):
    arr[i] = arr[i - 1] + diff[i]

print(max(arr))