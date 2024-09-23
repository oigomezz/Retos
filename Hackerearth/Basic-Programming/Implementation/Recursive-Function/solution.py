arr = [[0] * 1000 for _ in range(1000)]


def f(x, y):
    if x == 0:
        if arr[x][y] == 0:
            arr[x][y] = (y + 1) % 1000
        return arr[x][y]
    else:
        if y == 0:
            if arr[x][y] == 0:
                arr[x][y] = f(x - 1, 1)
            return arr[x][y]
        else:
            if arr[x][y] == 0:
                arr[x][y] = f(x - 1, f(x, y - 1))
            return arr[x][y]


if __name__ == "__main__":
    x, y = map(int, input().split())
    ans = f(x, y)

    a = ans % 10
    ans //= 10
    b = ans % 10
    ans //= 10
    c = ans % 10
    s = f"{c}{b}{a}"
    print(s)
