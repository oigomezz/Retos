from typing import List

MX = int(1e6)
arr = [0] * 40
n = 0
m = 0
factors = [[] for _ in range(MX + 1)]


def print_mat(matrix: List[List[bool]]):
    for row in matrix:
        print(" ".join(map(str, row)))


def mul_mat(a: List[List[bool]], b: List[List[bool]]) -> List[List[bool]]:
    r1, r2 = len(a), len(b)
    _, c2 = len(a[0]), len(b[0])
    ans = [[False] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                if a[i][k] and b[k][j]:
                    ans[i][j] = True
                    break
    return ans


def power_mat(mat: List[List[bool]], p: int) -> List[List[bool]]:
    if p == 1:
        return mat
    ans = power_mat(mat, p >> 1)
    ans = mul_mat(ans, ans)
    if p % 2:
        ans = mul_mat(mat, ans)
    return ans


def solve_movement() -> bool:
    mat = [[False] * n for _ in range(n)]
    for i in range(n):
        for f in factors[arr[i]]:
            if i + f < n:
                mat[i][i + f] = True
            if i - f >= 0:
                mat[i][i - f] = True
    mat = power_mat(mat, m)
    return mat[0][n - 1]


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in primes:
        for j in range(i, MX + 1, i):
            factors[j].append(i)

    t = int(input())
    for _ in range(t):
        global n, m, arr
        n = int(input())
        arr = list(map(int, input().split()))
        m = int(input())
        print("YES" if solve_movement() else "NO")


if __name__ == "__main__":
    main()
