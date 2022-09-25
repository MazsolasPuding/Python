def fib_list(ran):
    a = 0
    b = 1
    res = []
    for num in range(ran):
        res.append(a)
        a, b = b, a+b
    return res

print(fib_list(10))

def fib_descreet_num(pos):
    try:
        pos = int(pos)
    except ValueError:
        return "Enter a number as a parameter!"

    a, b = 0, 1
    for num in range(pos-1):
        a, b = b, a+b
    return a


print(fib_descreet_num(10))
# Standard list generating
list_of_fib1 = list(map(fib_descreet_num, range(1, 11)))
print(list_of_fib1)
#list comprehension
list_of_fib2 = [fib_descreet_num(x) for x in range(1, 11)]
print(list_of_fib2)

print(fib_descreet_num("lol"))