'''        1개 선착순 1단
1단 -> 2단  6개 선착순 2단
2단 -> 3단  12개 선착순 3단
3 -> 4단  18개 선착순
4단 -> 5단  24개 선착순
'''

n = int(input())
think = 1
dan = 1

if n == 1:
    print(1)
else:
    while n > think:
        think += 6 * dan
        dan += 1

    print(dan)


