T = int(input())
assert 1 <= T <= 100000
S = 0

for _ in range(T):
    N = int(input())
    assert 1 <= N <= 100000
    S += N
    A = list(map(int, input().split()))
    for a in A:
        assert 0 <= a <= 1000000000

    ans = 0
    s = set()
    j = 0
    for i in range(N):
        while j < N and A[j] not in s:
            s.add(A[j])
            j += 1
        ans += (j - i) * (j - i + 1) // 2
        s.remove(A[i])

    print(ans)

assert S <= 100000
