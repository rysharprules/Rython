def calculate(a, action, b):
    print('Performing ' + str(a) + ' ' + action + ' ' + str(b))
    if action == 'x':
        return a * b
    elif action == '+':
        return a + b
    elif action == '/':
        return a / b
    return a - b

paramA = int(input('Choose an integer... '))
action = input('Choose "x", "+", "/", or "-"... ')
paramB = int(input('Choose an integer... '))

print('The answer is ' + str(calculate(paramA, action, paramB)))