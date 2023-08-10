import re

expression = input()
pattern = r'(\d+|[+\-*/=])'
tokens = re.findall(pattern, expression)
operation = ['+', '-', '*', '/', '=']
result = int(tokens[0])

for i in range(1, len(tokens), 2):
    if tokens[i] in operation:
        if tokens[i] == '+':
            result += int(tokens[i + 1])
        elif tokens[i] == '-':
            result -= int(tokens[i + 1])
        elif tokens[i] == '*':
            result *= int(tokens[i + 1])
        elif tokens[i] == '/':
            result //= int(tokens[i + 1])
        elif tokens[i] == '=':
            break

print(result)
