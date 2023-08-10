n, k, d = input().split()
n = int(n)
k = int(k)
for i in range(1, n + 1):
    if d == 'L':
        print(' ' * (i - 1) + '*' * k)
    elif d == 'R':
        print(' ' * (n - i) + '*' * k)
