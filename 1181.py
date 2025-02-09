n = int(input())
lst = []

for _ in range(n):
    word = input()
    lst.append(word)

words = sorted(set(lst), key=lambda x: (len(x), x))

for word in words:
    print(word)

