from itertools import combinations

cards = []
lst = []

n, m = map(int, input().split())

cards = list(map(int, input().split()))

combi = combinations(cards, 3)

for j in combi:
    lst.append(sum(j))

flst = [num for num in lst if num < m]

if m in lst:
    print(m)

if m not in lst:
    print(max(flst))


