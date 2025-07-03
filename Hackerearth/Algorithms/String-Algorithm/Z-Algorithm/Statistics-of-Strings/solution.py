import sys

n, alp, mod = 0, 0, 0
pow_alp = [0] * 25
len_str = 0
p = [0] * 25
str_arr = [0] * 25
gl_ans = 0
used = [False] * 25


def add(a: int, b: int) -> int:
    return (a + b) % mod


def mul(a: int, b: int) -> int:
    return (a * b) % mod


def get_k() -> int:
    idx = len_str - 1
    if idx == 0:
        return 0
    k = p[idx - 1]
    while k > 0 and str_arr[idx] != str_arr[k]:
        k = p[k - 1]
    if str_arr[idx] == str_arr[k]:
        k += 1
    return k


def get_c(cur_alp: int) -> int:
    idx = len_str - 1
    if idx == 0:
        return -1
    if p[idx] != 0:
        return str_arr[p[idx] - 1]
    used[:cur_alp] = [False] * cur_alp
    k = p[idx - 1]
    while True:
        used[str_arr[k]] = True
        if k == 0:
            break
        k = p[k - 1]
    for c in range(cur_alp):
        if not used[c]:
            return c
    return -1


def get_used_cnt(cur_alp: int) -> int:
    if len_str == 1:
        return 0
    return sum(1 for i in range(cur_alp) if used[i])


def rec(cur_alp: int, cur_coef: int, cur_mx: int):
    global len_str, gl_ans
    prev_p = -1
    if len_str != 0:
        prev_p = p[len_str - 1]
    last = n - len_str
    if cur_mx >= prev_p + last:
        cur_ans = mul(cur_coef, cur_mx)
        cur_ans = mul(cur_ans, pow_alp[last])
        gl_ans = add(gl_ans, cur_ans)
        return
    len_str += 1
    for new_p in range(prev_p + 2):
        p[len_str - 1] = new_p
        new_alp = cur_alp
        c = get_c(new_alp)
        if c == -1:
            c = new_alp
            new_alp += 1
        str_arr[len_str - 1] = c
        k = get_k()
        if k == new_p and new_alp <= alp:
            new_coef = cur_coef
            if new_p == 0:
                used_cnt = get_used_cnt(cur_alp)
                new_coef = mul(new_coef, alp - used_cnt)
            rec(new_alp, new_coef, max(cur_mx, new_p))
    len_str -= 1


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split()
    n, alp, mod = map(int, input_data)
    pow_alp[0] = 1
    for i in range(1, 25):
        pow_alp[i] = mul(pow_alp[i - 1], alp)
    rec(0, 1, 0)
    print(gl_ans)
