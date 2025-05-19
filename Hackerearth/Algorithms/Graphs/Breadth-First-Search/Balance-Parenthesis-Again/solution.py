import heapq


if __name__ == "__main__":
    n = int(input())
    s = input()
    opening = []
    closing = []
    sequence = [0] * (n + 1)

    for i in range(1, n + 1):
        sequence[i] = i

    for i in range(n):
        if s[i] == '(':
            heapq.heappush(opening, i + 1)
        else:
            heapq.heappush(closing, i + 1)

    if opening:
        prev = heapq.heappop(opening)
        while opening:
            print(prev, heapq.heappop(opening))
            prev = opening[0] if opening else None

        if closing:
            print(prev, heapq.heappop(closing))
            prev = closing[0] if closing else None

        while closing:
            print(prev, heapq.heappop(closing))
            prev = closing[0] if closing else None
    else:
        prev = heapq.heappop(closing)
        while closing:
            print(prev, heapq.heappop(closing))
            prev = closing[0] if closing else None
