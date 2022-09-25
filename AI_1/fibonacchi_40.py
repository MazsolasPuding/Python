def fibo(n):
    fib = [1, 1]
    for i in range(n-2):
        add = fib[i] + fib[i+1]
        fib.append(add)
        if len(fib) == 20:
            print("lol")
    return fib


print(fibo(40))


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
