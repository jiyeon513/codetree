n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
arr = ['']*200001
curr = 100000

for i in range(n):
    step = x[i]
    if dir[i]=='L':
        while step > 0:
            arr[curr]='W'
            step-=1
            if step:
                curr-=1
    if dir[i]=='R':
        while step > 0:
            arr[curr]='B'
            step-=1
            if step:
                curr+=1

print(arr.count('W'), arr.count('B'))
