a, b, c = map(int, input().split())

if a == b == c :
    print(10000 + (a * 1000))
elif a == b and a != c:
    print(1000 + a * 100)
elif b == c and b != a:
    print(1000 + b * 100)
elif a == c and a != b:
    print(1000 + a * 100)
elif a != b and a != c and b != c :
    print((max(a, b, c)) * 100)

