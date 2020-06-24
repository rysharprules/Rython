def fizzbuzz(max, rules):
    fizz = 'Fizz'
    buzz = 'Buzz'
    bong = 'Bong'
    bang = 'Bang'

    for index in range(1, max + 1):
        fezz = ''
        reverse = False
        if rules[13] and index % 13 == 0:
            fezz = 'Fezz' 
        if rules[17] and index % 17 == 0:
            reverse = True
        if (rules[5] and rules[3]) and index % 15 == 0:
            fifteen = fizz + fezz + buzz
            if reverse:
                fifteen = buzz + fezz + fizz
            print(fifteen)
        elif (rules[3] and rules[7]) and index % 21 == 0:
            twentyone = fizz + fezz + bang
            if reverse:
                twentyone = bang + fezz + fizz
            print(twentyone)
        elif rules[11] and index % 11 == 0:
            eleven = fezz + bong
            if reverse:
                eleven = bong + fezz
            print(eleven)
        elif rules[3] and index % 3 == 0:
            print(fizz)
        elif rules[5] and index % 5 == 0:
            five = fezz + buzz
            if reverse:
                five = buzz + fezz
            print(five)
        elif rules[7] and index % 7 == 0:
            seven = fezz + bang
            if reverse:
                seven = bang + fezz
            print(seven)
        else:
            if len(fezz) > 0:
                print(fezz)
                continue
            print(index)

max = int(input('Choose a maximum number...'))
rules = {3: False, 5: False, 7: False, 11: False, 13: False, 17: False}
for key in rules.keys():
    if input('Press y if you would like to activate the rule for ' + str(key) 
    + ' - otherwise, press any other key. >>> ') == 'y':
        rules[key] = True
        continue
fizzbuzz(max, rules)