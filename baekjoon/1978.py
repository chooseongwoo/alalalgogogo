n = int(input())
lst = list(map(int, input().split(' ')))
cnt = 0

for i in lst:
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                break
            cnt += 1
print(cnt)