def gifts(n, s, k):
    s = sorted(s)
    result = sum(s[:k])
    result += s[k - 1] * (n - k)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = map(int, input().split())
    k = int(input())

    out_ = gifts(n, s, k)
    print(out_)
