n, c = map(int, input().split())
students = list(map(int, input().split()))

students.sort()

for i in range((n // c) + 1):
    for j in range(c * i, c * i + c):
        if j > len(students):
            break
        print(students[j], end=' ')
    print()