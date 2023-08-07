num = int(input())
onum = ''

if num % 10 == 1:
    onum = str(num) + 'st'
    if num == 11:
        onum = str(num) + 'th'
elif num % 10 == 2:
    onum = str(num) + 'nd'
    if num == 12:
        onum = str(num) + 'th'
elif num % 10 == 3:
    onum = str(num) + 'rd'
    if num == 13:
        onum = str(num) + 'th'
else:
    onum = str(num) + 'th'
print(onum)