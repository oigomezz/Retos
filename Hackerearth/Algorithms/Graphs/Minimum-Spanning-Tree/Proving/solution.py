from typing import List
import sys

MOD = 1000000007
suma = 0
par = [0] * 1000010


def mult(c: List[int], a: List[int], b: List[int]) -> None:
    x1 = (a[0] * b[0] + a[1] * b[2]) % MOD
    x2 = (a[0] * b[1] + a[1] * b[3]) % MOD
    x3 = (a[2] * b[0] + a[3] * b[2]) % MOD
    x4 = (a[2] * b[1] + a[3] * b[3]) % MOD
    c[0] = x1
    c[1] = x2
    c[2] = x3
    c[3] = x4


def fib(n: int) -> int:
    res = [1, 0, 0, 1]
    c = [1, 1, 1, 0]
    while n > 0:
        if n & 1:
            mult(res, res, c)
        mult(c, c, c)
        n //= 2
    return res[1]


def find_par(x: int) -> int:
    if x == par[x]:
        return x
    par[x] = find_par(par[x])
    return par[x]


def init(n: int) -> None:
    for i in range(n):
        par[i] = i


if __name__ == "__main__":
    line = list(map(str.strip, input().split()))

    n = int(line[0])
    assert 1 <= n <= 1000
    init(n * n)

    k1 = int(line[1])
    k2 = int(line[2])
    k3 = int(line[3])
    k4 = int(line[4])

    assert 1 <= k1 <= 1000000000000000000
    assert 1 <= k2 <= 1000000000000000000
    assert 1 <= k3 <= 1000000000000000000
    assert 1 <= k4 <= 1000000000000000000

    fk1 = fib(k1)
    fk2 = fib(k2)
    fk3 = fib(k3)
    fk4 = fib(k4)
    fk_1 = fib(k1 - 1)
    fk_2 = fib(k2 - 1)
    fk_3 = fib(k3 - 1)
    fk_4 = fib(k4 - 1)

    graph = []
    for i in range(n):
        for j in range(n):
            u = n * i + j
            if j < n - 1:
                v = n * i + j + 1
                w = (fk1 + fk2) % MOD
                tmp = fk1
                fk1 += fk_1
                if fk1 >= MOD:
                    fk1 %= MOD
                fk_1 = tmp
                tmp = fk2
                fk2 += fk_2
                if fk2 >= MOD:
                    fk2 %= MOD
                fk_2 = tmp
                graph.append((w, (u, v)))

    for j in range(n):
        for i in range(n):
            u = n * i + j
            if i < n - 1:
                v = n * (i + 1) + j
                w = (fk3 + fk4) % MOD
                graph.append((w, (u, v)))
                tmp = fk3
                fk3 += fk_3
                if fk3 >= MOD:
                    fk3 %= MOD
                fk_3 = tmp
                tmp = fk4
                fk4 += fk_4
                if fk4 >= MOD:
                    fk4 %= MOD
                fk_4 = tmp

    graph.sort()
    for i in range(len(graph)):
        pu = find_par(graph[i][1][0])
        pv = find_par(graph[i][1][1])
        if pu != pv:
            suma += graph[i][0]
            par[pu] = pv

    print(suma)
