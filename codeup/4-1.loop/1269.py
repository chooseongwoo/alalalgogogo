a, b, c, n = map(int, input().split())

number = a
for i in range(1, n):
    number = number * b + c
print(number)