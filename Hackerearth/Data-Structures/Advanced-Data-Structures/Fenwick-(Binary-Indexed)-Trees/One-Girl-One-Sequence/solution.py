fen = [0] * 1000008
n = 0


def add(ind, x):
    global n
    while ind <= n:
        fen[ind] += x
        ind += ind & -ind


def get(ind):
    sum_ = 0
    while ind:
        sum_ += fen[ind]
        ind -= ind & -ind
    return sum_


def main():
    global n
    n, x = map(int, input().split())
    a = [(0, 0)] * n
    line = list(map(int, input().split()))

    for i in range(n):
        a[i] = (line[i], i + 1)

    a.sort()
    ans = x * n
    inv = 0

    for i in range(n, 0, -1):
        ind = a[i - 1][1]
        inv += get(ind - 1)
        ans = min(ans, x * (i - 1) + inv)
        add(ind, 1)

    print(ans)


if __name__ == "__main__":
    main()
