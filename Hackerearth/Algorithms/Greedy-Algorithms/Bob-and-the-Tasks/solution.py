def minimum_days(n, k, a):
    s = set()
    for i in range(n):
        s.add(a[i])
        if len(s) > 1:
            second_largest = sorted(s)[-2]
            if sorted(s)[-1] - second_largest - 1 == k:
                return i + 1
        last_element = sorted(s)[-1] if s else None
        if last_element is not None and last_element - sorted(s)[-1] - 1 == k:
            return i + 1
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(minimum_days(n, k, a))
