a = int(input())
b = int(input())
lst = list(map(int, input().split()))
result = a

for i in lst:
    result *= (1 + i * 0.01)

profit = round(result - a)
print(profit)
if profit > 0:
    print('good')
elif profit == 0:
    print('same')
else:
    print('bad')