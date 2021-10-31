def fib(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
for elem in fib(10):
    print(elem, end = ' ')
