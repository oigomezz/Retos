def main():
    s = input().strip()
    c = input().strip()
    p = int(input().strip())

    n = len(s)
    assert 1 <= n <= 1000
    for char in s:
        assert 'a' <= char <= 'z'
    assert 'a' <= c <= 'z'
    assert 1 <= p <= n

    cnt = sum(1 for i in range(p) if s[i] == c)
    z = cnt

    for i in range(p, n):
        cnt -= (s[i - p] == c)
        cnt += (s[i] == c)
        z = max(z, cnt)

    if z == p:
        print("-1")
        return

    p -= 1
    cnt = sum(1 for i in range(p) if s[i] == c)
    idx = -1

    if cnt == z:
        idx = p

    for i in range(p, n):
        cnt -= (s[i - p] == c)
        cnt += (s[i] == c)
        if cnt == z:
            idx = i + 1

    print(idx)


if __name__ == "__main__":
    main()
