n = int(input())

for i in range(n):
    num = sum(map(int, str(i)))
    temp = num + i

    if temp == n:
        print(i)
        break
else:
        print(0)