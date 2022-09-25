def solution(n):

    place_value = []
    num = n
    result = ""

    while num != 0:
        place_value.append(num % 10)
        num = num // 10

    place_value.reverse()
    print(place_value)
    zero = place_value[0]

    if len(place_value) > 3:
        for i in range(n // 1000):
            result += 'M'
        for i in range(len(place_value[:-3])):
            del place_value[0]
        print(place_value)

    if len(place_value) > 2:
        zero = place_value[0]
        print(zero)
        if zero <= 3:
            for i in range(zero):
                result += 'C'
        elif zero == 4:
            result += 'CD'
        elif zero >= 5 and zero < 9:
            result += 'D'
        if zero >= 6 and zero <= 8:
            for i in range(zero - 5):
                result += 'C'
        elif zero == 9:
            result += 'CM'
        del place_value[0]
        print(place_value)

    if len(place_value) > 1:
        zero = place_value[0]
        print(zero)
        if zero <= 3:
            for i in range(zero):
                result += 'X'
        elif zero == 4:
            result += 'XL'
        elif zero >= 5 and zero < 9:
            result += 'L'
        if zero >= 6 and zero <= 8:
            for i in range(zero - 5):
                result += 'X'
        elif zero == 9:
            result += 'XC'
        del place_value[0]
        print(place_value)

    if len(place_value) > 0:
        zero = place_value[0]
        print(zero)
        if zero <= 3:
            for i in range(zero):
                result += 'I'
        elif zero == 4:
            result += 'IV'
        elif zero >= 5 and zero < 9:
            result += 'V'
        if zero >= 6 and zero <= 8:
            for i in range(zero - 5):
                result += 'I'
        elif zero == 9:
            result += 'IX'
        del place_value[0]
        print(place_value)

    print(result)


solution(1666)
