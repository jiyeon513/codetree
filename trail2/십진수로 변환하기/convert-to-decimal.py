binary = input()

# Please write your code here.
num = 0
arr = list(map(int, binary))

for i in range(len(arr)):
    num = num*2 + arr[i]

print(num)