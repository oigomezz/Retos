def fibonacci(num):
    n0 = 0
    n1 = 1
    for _ in range(1, num):
        print(n0)
        fib = n0 + n1
        n0 = n1
        n1 = fib

fibonacci(51)