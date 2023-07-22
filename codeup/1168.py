a,b = input().split()
b = int(b)

if b == 1 or b == 2:
    birth_year = int('19' + a[0:2])
    print(2012 - birth_year + 1)

elif b == 3 or b == 4:
    birth_year = int('20' + a[0:2])
    print(2012 - birth_year + 1)