def factorial(n):
    if n < 0:
        return None
    elif n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


no_factorial = "No tiene factorial"
print(factorial(0) or no_factorial)
print(factorial(7) or no_factorial)
print(factorial(10) or no_factorial)
print(factorial(1) or no_factorial)
print(factorial(-1) or no_factorial)
