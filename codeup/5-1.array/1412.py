lst = input()

count_dict = {}

for i in lst:
    if i.isalpha():
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

for char in "abcdefghijklmnopqrstuvwxyz":
    if char in count_dict:
        print(f'{char}:{count_dict[char]}')
    else:
        print(f'{char}:0')
