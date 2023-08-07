a, b, c = map(int, input().split())

if a <= 170:
    print(f'CRASH {a}')
elif b <= 170:
    print(f'CRASH {b}')
elif c <= 170:
    print(f'CRASH {c}')
else:
    print('PASS')