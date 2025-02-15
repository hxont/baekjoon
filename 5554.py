sum = 0
for i in range(4):
    n = int(input())
    sum += n

if sum % 60 == 0:
    x = sum // 60
    y = 0

if sum % 60 != 0:
    x = sum // 60
    y = sum % 60

print(x)
print(y)
