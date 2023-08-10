n = int(input())

for i in range(n):
    if n >= i**2 and n<(i+1)**2:
        k = n - i**2
        t = i
        break
print(k, t)