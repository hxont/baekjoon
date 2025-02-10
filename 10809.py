s = list(input())
az = 'abcdefghijklmnopqrstuvwxyz'

for i in az:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

