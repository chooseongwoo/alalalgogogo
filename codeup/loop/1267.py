n = int(input())
numbers = list(map(int, input().split()))
sum = 0
for i in numbers:
    if i % 5 == 0:
        sum += i
print(sum)