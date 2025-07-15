MOD = 1000000007
T = int(input())
assert 1 <= T <= 10
for _ in range(T):
    str_num = input()
    sum_arr = [1, 0, 0]
    ans = 0
    len_str = len(str_num)
    assert 1 <= len_str <= 1000000

    for char in str_num:
        dig = int(char)
        sumt = [0, 0, 0]
        assert '0' <= char <= '9'

        if dig % 2 == 0:
            off = (3 - dig % 3) % 3
            ans = (ans + sum_arr[off]) % MOD

        for j in range(3):
            sumt[(j + dig) % 3] = (sumt[(j + dig) % 3] + sum_arr[j]) % MOD

        for j in range(3):
            sum_arr[j] = (sum_arr[j] + sumt[j]) % MOD

    print(ans)
