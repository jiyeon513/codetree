n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)


loc = 0
OFFSET=1000
arr = [0]*2001   

# Please write your code here.
for i in range(n):
    step = x[i]
    if dir[i]=='R':
        for _ in range(step):
            arr[loc+OFFSET]+=1
            loc+=1
    if dir[i]=='L':
        for _ in range(step):
            loc-=1
            arr[loc+OFFSET]+=1
            

count = 0
for i in arr:
    if i >= 2:
        count+=1

print(count)

        
        