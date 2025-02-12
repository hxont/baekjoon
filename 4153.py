while True:
    lst = list(map(int, input().split()))
    slst = sorted(lst)

    if slst[0] != 0 and slst[1] != 0 and slst[2] != 0:
        if slst[0]**2 + slst[1]**2 == slst[2]**2:
            print('right')
        else:
            print('wrong')

    if slst[0] == 0 and slst[1] == 0 and slst[2] == 0:
        break
