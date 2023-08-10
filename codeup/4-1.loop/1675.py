a = list(input())
c = []
s = ' '

for i in range(0, len(a)):
    if a[i] == s:
        c = a[i]
    else:
        if a[i] != s:
            c = ord(a[i])
            if c >= 97 and c <= 99:
                c = chr((c - 3) + 26)
            else:
                c = chr(c - 3)
        else:
            continue
    print(c, end='')
