a, b = map(int, input().split())
n = input()

# Please write your code here.

digits = list(map(int, n))
num = 0

for i in range (len(digits)):
    num = num * a + digits[i]

result = []

while True:
    if num < b:
        result.append(num)
        break
    result.append(num%b)
    num//=b

for i in result[::-1]:
    print(i, end="")