import random


def get_num(v):
    n = len(v)
    index = random.randint(0, n - 1)
    num = v[index]
    v[index], v[n - 1] = v[n - 1], v[index]
    v.pop()
    return num


def generate_random(n):
    v = list(range(1, n + 1))
    while v:
        print(get_num(v), end=" ")


if __name__ == "__main__":
    n, k = map(int, input().split())
    a_list = [int(input()) for _ in range(n)]
    d = 0
    c = 1
    while d < k - 1:
        if n - c > k - d + 4:
            c += 5
        elif n - c > k - d + 3:
            c += 4
        elif n - c > k - d + 2:
            c += 3
        elif n - c > k - d + 1:
            c += 2
        else:
            c += 1
        d += 1
        print(c)
    print(n)
    generate_random(k)
