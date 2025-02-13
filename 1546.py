n = int(input())
lst = list(map(int, input().split()))
sum = 0

for i in lst :
    sum += (i/max(lst)) * 100

print(sum/n)
