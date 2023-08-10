n = int(input())
nums = list(map(int, input().split()))
max = 0
for i in nums:
    if max < i:
        max = i
print(max)