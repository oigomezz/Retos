import math

g, x, y = 0, 0, 0


def extended_euclid(a, b):
    global g, x, y
    if b == 0:
        g = a
        x = 1
        y = 0
    else:
        extended_euclid(b, a % b)
        temp = x
        x = y
        y = temp - (a // b) * y


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        a, b, d = map(int, input().split())
        extended_euclid(a, b)

        if d % g != 0:
            print("0")
            continue

        k1 = math.ceil(-x * (d / b))
        k2 = math.floor(y * (d / a))
        if k1 <= k2:
            print(str(k2 - k1 + 1))
        else:
            print("0")
