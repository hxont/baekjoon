num = list(map(int, input().split()))
checka = False
checkd = False

for i in range(len(num) - 1):
        if num[i] > num[i+1]:
            checkd = True
        elif num[i] < num[i+1]:
            checka = True

if checka and checkd:
    print('mixed')
elif checka == True:
    print('ascending')
elif checkd == True:
    print('descending')
