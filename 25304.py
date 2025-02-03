X = int(input())
N = int(input())
bank = 0

for i in range(N):
    a, b = map(int, input().split())
    bank += a * b

if X == bank:
    print("Yes")
else:
    print("No")
