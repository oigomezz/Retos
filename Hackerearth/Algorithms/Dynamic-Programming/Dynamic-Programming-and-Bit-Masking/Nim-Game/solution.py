f = [[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]
      for _ in range(2)] for _ in range(64)]


def solve(size, tar, bit, carry, small_i, small_j, non_zero_i):
    if bit == 63:
        return int(small_i and small_j and non_zero_i and carry == 0)
    ret = f[bit][small_i][small_j][carry][non_zero_i]
    if ret != -1:
        return ret
    ret = 0
    for idx1 in range(2):
        for idx2 in range(2):
            ij = (idx1 + idx2 + carry) % 2
            new_carry = (idx1 + idx2 + carry) // 2
            new_small_i = idx1 < idx2 or (idx1 == idx2 and small_i)
            new_small_j = idx2 < ((size >> bit) & 1) or (
                idx2 == ((size >> bit) & 1) and small_j)
            new_non_zero = non_zero_i or (idx1 > 0)
            if (idx1 ^ idx2 ^ ij) == ((tar >> bit) & 1):
                ret += solve(size, tar, bit + 1, new_carry,
                             new_small_i, new_small_j, new_non_zero)
                ret %= 1000000007
    f[bit][small_i][small_j][carry][non_zero_i] = ret
    return ret


if __name__ == "__main__":
    tests = int(input().strip())
    for _ in range(tests):
        n = int(input().strip())
        if n % 4 == 1 or n % 4 == 2:
            print("0")
        else:
            target = n if n % 4 == 0 else 0
            for i in range(64):
                for j in range(2):
                    for k in range(2):
                        for l in range(2):
                            for m in range(2):
                                f[i][j][k][l][m] = -1
            print(solve(n, target, 0, 0, False, True, False))
