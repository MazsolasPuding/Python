
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


arr = list(range(10))
print(arr)
res = list(map(fib, arr))
print(res)


