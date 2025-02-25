import sys

n = int(sys.stdin.readline())
nlst = []

for i in range(n):
    num = int(sys.stdin.readline())
    nlst.append(num)

snlst = sorted(nlst)

for item in snlst:
    print(item)

