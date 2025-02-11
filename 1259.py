while True:
    n = int(input())
    ntr = str(n)

    if n != 0:
        if ntr == ntr[::-1]:
            print('yes')
        else:
            print('no')

    if n == 0:
        break
