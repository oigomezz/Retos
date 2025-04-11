t = int(input())
for _ in range(t):
    n = list(input().strip())
    n.sort()
    even_sum = int(''.join(n[0::2]))
    odd_sum = int(''.join(n[1::2]))
    print(even_sum + odd_sum)
