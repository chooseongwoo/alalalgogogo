n = int(input())
students = list(map(int, input().split()))

students.reverse()
for i in students:
    print(i, end=' ')