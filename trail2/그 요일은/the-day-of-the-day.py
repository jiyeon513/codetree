m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
dates = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total1 = 0
for i in range(1, m1):
    total1 += month[i]
total1 += d1

total2 = 0
for i in range(1, m2):
    total2 += month[i]
total2 += d2

diff = total2 - total1

offset = dates.index(A)
if diff < offset:
    print(0)
else:
    print(1 + (diff - offset) // 7)