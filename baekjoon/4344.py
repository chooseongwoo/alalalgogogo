n = int(input())

for _ in range(n):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / lst[0]

    cnt = 0
    for i in lst[1:]:
        if i > avg:
            cnt += 1
    per = (cnt/lst[0]) * 100
    print(str(round(per,3))+ '%')