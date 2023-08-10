lst = [[], []]
max_value = -1000000
min_value = 1000000

for _ in range(5):
    n = int(input())
    if n > max_value:
        max_value = n
    if n < min_value:
        min_value = n

lst[0].append(max_value)
lst[1].append(min_value)

print(lst[0][0])
print(lst[1][0])
