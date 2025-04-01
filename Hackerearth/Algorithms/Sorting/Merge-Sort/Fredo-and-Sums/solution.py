t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().strip().split()))
    even_sum = sum(a[0::2])
    odd_sum = sum(a[1::2])
    first_half_sum = sum(a[:n // 2])
    second_half_sum = sum(a[n // 2:])
    print(odd_sum - even_sum, second_half_sum - first_half_sum)
