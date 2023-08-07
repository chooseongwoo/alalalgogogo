n = list(map(int, input().split()))

for i in n:
    if i % 5 == 0:
        print(i)
        break
else:
    print(0)