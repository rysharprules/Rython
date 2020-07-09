def calculate(a, action, b):
    print('Performing ' + str(a) + ' ' + action + ' ' + str(b))
    if action == 'x':
        return a * b
    elif action == '+':
        return a + b
    elif action == '/':
        return a / b
    return a - b

with open("file/step_2.txt", 'r') as f:
    calcs = f.read().splitlines()

total = 0

for calc in calcs:
    operation = calc.split()
    answer = calculate(int(operation[2]), operation[1], int(operation[3]))
    total += answer
    print('Answer = ' + str(answer))

print('Total is = ' + str(total))