n, k = map(int, input().split())
for i in range(0, k):
    ans = 0
    i = 1

    while n // i > 0:
        temp = (n//(i * 10))*i + (n % i)
        i *= 10
        if temp > ans:
            ans = temp

    n = ans
print(ans)
