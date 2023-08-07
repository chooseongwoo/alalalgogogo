a, b = map(float, input().split())

i = a
while i <= b:
    print('%.2f' % i)
    i += 0.01
