lotto = list(map(int, input().split()))
pick = list(map(int, input().split()))
count = 0

win_num = lotto[:6]
bonus_num = lotto[-1]
bonused = False

for i in pick:
    if i in win_num:
        count += 1

if bonus_num in pick:
    bonused = True

if count == 6:
    print(1)
elif count == 5 and bonused:
    print(2)
elif count == 5:
    print(3)
elif count == 4:
    print(4)
elif count == 3:
    print(5)
else:
    print(0)