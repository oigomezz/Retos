from collections import defaultdict

t = int(input())
results = []
for _ in range(t):
    n, q = map(int, input().split())
    v = [0] * (n + 1)
    board = defaultdict(int)
    arr = list(map(int, input().split()))

    for i in range(1, n + 1):
        v[i] = arr[i-1]
        board[v[i]] += 1

    for _ in range(q):
        l, r = map(int, input().split())
        board[v[l]] -= 1
        if board[v[l]] == 0:
            del board[v[l]]
        v[l] = r
        board[v[l]] += 1

        results.append(str(len(board) + 1))

print("\n".join(results))
