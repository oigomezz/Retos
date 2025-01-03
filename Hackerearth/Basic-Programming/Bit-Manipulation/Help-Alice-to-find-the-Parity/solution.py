def get_xor(n):
    mod = n % 4
    if 0 == mod:
        return n
    elif 1 == mod:
        return 1
    elif 2 == mod:
        return n + 1
    elif 3 == mod:
        return 0


def find_x(a, b):
    return get_xor(a - 1) ^ get_xor(b)


l, r = map(int, input().strip().split())
x = find_x(l, r)
if x % 2:
    print("odd")
else:
    print("even")
