a, b = map(int, input().split())
result = 0
lst = []
for i in range(a, b + 1):
    if i % 2 == 0:
        lst.append('-' + str(i))
        result -= i
    else:
        if a == i:
            lst.append(str(i))
            result += i
        else:
            lst.append('+' + str(i))
            result += i
print(''.join(lst) + '=' + str(result))