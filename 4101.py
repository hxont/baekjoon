while True:
    try:
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break

        elif a > b:
            print('Yes')
        elif a == b:
            print('No')
        elif a < b:
            print('No')
    except :
        break
