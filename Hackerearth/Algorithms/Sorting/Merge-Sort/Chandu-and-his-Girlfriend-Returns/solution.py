t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = input().strip().split()
    b = input().strip().split()
    combined = a + b
    sorted_combined = sorted(combined, key=int, reverse=True)
    print(*sorted_combined)
