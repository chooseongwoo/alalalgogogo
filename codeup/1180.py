n = int(input())
push = int(str(n)[::-1]) * 2

if push >= 100:
    push %= 100

if push <= 50:
    print(push)
    print('GOOD')
else:
    print(push)
    print('OH MY GOD')