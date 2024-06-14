def solve(x):
    ch = "."
    l = len(x)
    TLD = ""
    alpha = False

    a = x.split(ch, 1)[0]
    b = x.split(ch, l)[-1]

    b_length = len(b)
    a_length = len(a)

    if b.isalpha():
        TLD = b

    tld_len = len(TLD)
    if tld_len == b_length:
        alpha = True

    if a.startswith("-") or a.endswith("-") or b.endswith("-") or alpha == False or b_length < 2:
        return "false"
    elif (a_length < 1) or a.startswith("a-z" or "0-9"):
        return "true"
    else:
        return "true"


T = int(input())

for _ in range(T):
    x = input()
    out_ = solve(x)
    print(out_)
