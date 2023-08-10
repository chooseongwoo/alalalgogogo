n = int(input())
lst = []

for i in range(2, n):
    if n % i == 0:
        lst.append(i)

if len(lst) == 2:
    if 4 in lst:
        print('wrong number')
    else:
        print(*lst)
else:
    print('wrong number')