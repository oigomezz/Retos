n, q = map(int, input().split())
a = set(map(int, input().split()))
queries = [int(input()) for _ in range(q)]
for query in queries:
    print("YES" if query in a else "NO")
