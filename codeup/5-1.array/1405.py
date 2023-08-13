n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        print(lst[i + j - n], end=' ')
    print()