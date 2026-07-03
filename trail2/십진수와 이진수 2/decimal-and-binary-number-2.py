N = input()

# Please write your code here.
arr= list(map(int, N))
num = 0

for i in range(len(arr)):
    num = num*2 +arr[i]


num=num*17


digits = []

while True:
    if num < 2:
        digits.append(num)
        break
    digits.append(num%2)
    num//=2

for digit in digits[::-1]:
    print(digit, end="")