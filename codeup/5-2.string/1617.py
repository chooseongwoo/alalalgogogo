num = input()
password = int(num) + int(str(num)[::-1])

if str(password) == str(password)[::-1]:
    print("YES")
else:
    print("NO")