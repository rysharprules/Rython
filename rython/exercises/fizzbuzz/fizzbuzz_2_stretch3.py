def fizzbuzz(max, rules):
    print('Chosen rules: ' + str(rules))
    for index in range(1, max + 1):
        match = False
        text = ''
        for ruleNumber, ruleText in rules.items():
            if index % ruleNumber == 0:
                text = text + ruleText
                match = True
        if match:
            print(text)
        else:
            print(index)

max = int(input('Choose a maximum number... '))
numberOfRules = int(input('Choose how many rules you want... '))
rules = {}
for index in range(numberOfRules):
    ruleNumber = int(input('Choose a number for the text to appear on... '))
    ruleText = input('Choose text to occur on that number... ')
    rules[ruleNumber] = ruleText
fizzbuzz(max, rules)