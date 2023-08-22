n = int(input())
students = list(map(int, input().split()))
count = [0] * 24

for i in range(n):
    count[students[i]] += 1

for i in range(1, 24):
    print(count[i], end=' ')