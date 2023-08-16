string = input()
cnt = 0
for i in range(len(string)):
    if string[i:i+4] == 'love':
        cnt += 1

print(cnt) 