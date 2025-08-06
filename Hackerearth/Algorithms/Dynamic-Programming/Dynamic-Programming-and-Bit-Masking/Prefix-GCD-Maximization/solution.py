from math import gcd


def solve(mask, arr, dyp):
    size = len(arr)
    if mask == (1 << size) - 1:
        return 0
    current_gcd = 0
    value = dyp[mask]
    if value != -1:
        return value
    value = 0
    for i in range(size):
        if mask & (1 << i):
            current_gcd = gcd(current_gcd, arr[i])
    for i in range(size):
        if (mask & (1 << i)) == 0:
            value = max(value, gcd(
                current_gcd, arr[i]) + solve(mask + (1 << i), arr, dyp))
    dyp[mask] = value
    return value


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    dp = [-1] * (1 << n)
    print(solve(0, array, dp))
