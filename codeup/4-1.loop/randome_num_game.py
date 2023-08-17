import random

random_number = random.randint(1, 100)
cnt = 0
while True:
    try:
        n = int(input())
    except:
        print("ㅄ")
        continue
    cnt += 1
    if random_number > n:
        print('UP!')
    elif random_number < n:
        print('DOWN!')
    else:
        print(cnt)
        break