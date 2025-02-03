from math import sqrt

n = int(input())
nums = list(map(int, input().split()))

def is_prime(number: int):
    if number == 1:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

cnt = 0
for i in nums:
    if is_prime(i):
        cnt += 1

print(cnt)
