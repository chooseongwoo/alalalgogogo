n = int(input())
students = list(map(int, input().split()))
lst = [0] * 23
for i in students:
    lst[i - 1] += 1
for i in lst:
    print(i, end=' ')