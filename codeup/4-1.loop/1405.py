n = int(input())
lst = list(map(int, input().split()))

for i in lst:
    print(*lst)
    lst.append(lst.pop(0))
