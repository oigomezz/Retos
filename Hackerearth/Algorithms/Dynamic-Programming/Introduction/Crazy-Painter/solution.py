t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().strip().split()))
    total_points = n * 12
    freq, additional = divmod(total_points, 26)
    ans = 0
    if freq > 0:
        ans += sum(c) * freq + freq * (freq - 1) // 2 * 26
        ans += sum(c[:additional]) + freq * additional
    else:
        ans += sum(c[:additional])
    print(ans)
