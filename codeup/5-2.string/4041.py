n = int(input())
print(int(str(n)[::-1]))

sum = 0
for i in str(n):
    sum += int(i)
print(sum)