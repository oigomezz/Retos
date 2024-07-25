from collections import Counter

for _ in range(int(input())):
    n = int(input())
    total = countries = 0

    q = list(map(int, input().split()))
    values = Counter(q)
    q = list(set(q))

    for i in q:
        if values[i] % i == 0:
            total += i*(values[i]//i)
            countries += values[i]//i

    print('Invalid Data') if (n != total) else print(countries)
