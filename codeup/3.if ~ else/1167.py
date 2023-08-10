a, b, c = map(int, input().split())

if a>=b:
    if b>=c:
        print(b)
    elif c>=a:
        print(a)
    else:
        print(c)
elif a>c:
    print(a)
elif b>c:
    print(c)
else:
    print(b)
