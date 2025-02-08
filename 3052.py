st = set()

for i in range(10):
    num = int(input())
    divide = num % 42
    st.add(divide)

print(len(st))


