n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0]*200
for a,b in segments:
    for i in range(a,b):
        arr[i+100]+=1

print(max(arr))