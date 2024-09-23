t = int(input())
while t > 0:
    n = int(input())
    A = [0] * 10

    while n > 0:
        c = n % 10
        n //= 10
        A[c] += 2

    x = 0
    max_count = float('-inf')

    for i in range(10):
        if max_count < A[i]:
            max_count = A[i]
            x = i

    print(x)
    t -= 1
