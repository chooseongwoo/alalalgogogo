n = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for i in numbers:
    if i % 2 == 1:
        cnt += 1
print(cnt)