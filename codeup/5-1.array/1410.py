rhkfgh = input()
l = 0
r = 0
for i in range(len(rhkfgh)):
    if rhkfgh[i] == '(':
        l += 1
    elif rhkfgh[i] == ')':
        r += 1
print(l, r)