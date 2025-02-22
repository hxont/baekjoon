import math

a, b, v = map(int, input().split())
days = math.ceil((v - a) / (a - b)) + 1
print(days)
