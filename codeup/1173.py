h, m = map(int, input().split())

if 1<=h<=23:
    if m>=30:
        print(h, m-30)
    else:
        print(h-1,m+30)
else:
    if m>=30:
        print(h, m-30)
    else:
        print(23,m+30)
    