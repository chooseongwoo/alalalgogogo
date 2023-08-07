time, a, b = map(int, input().split())

goal = (89 - time) // 5 + 1

if a + goal > b:
    print('win')
elif a + goal == b:
    print('same')
else:
    print('lose')