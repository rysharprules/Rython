def fizzbuzz(max = 100):
    fizz = 'Fizz'
    buzz = 'Buzz'
    bong = 'Bong'
    bang = 'Bang'

    for index in range(1, max + 1):
        fezz = ''
        reverse = False
        if index % 13 == 0:
            fezz = 'Fezz' 
        if index % 17 == 0:
            reverse = True
        if index % 15 == 0:
            fifteen = fizz + fezz + buzz
            if reverse:
                fifteen = buzz + fezz + fizz
            print(fifteen)
        elif index % 21 == 0:
            twentyone = fizz + fezz + bang
            if reverse:
                twentyone = bang + fezz + fizz
            print(twentyone)
        elif index % 11 == 0:
            eleven = fezz + bong
            if reverse:
                eleven = bong + fezz
            print(eleven)
        elif index % 3 == 0:
            print(fizz)
        elif index % 5 == 0:
            five = fezz + buzz
            if reverse:
                five = buzz + fezz
            print(five)
        elif index % 7 == 0:
            seven = fezz + bang
            if reverse:
                seven = bang + fezz
            print(seven)
        else:
            if len(fezz) > 0:
                print(fezz)
                continue
            print(index)

fizzbuzz(int(input('Choose a maximum number...')))