def decode(s):
    ln = len(s)
    if ln == 1:
        return s
    else:
        return s[ln - 2::-2] + s[1 - ln % 2::2]


T = int(input())
for _ in range(T):
    s = input()
    out_ = decode(s)
    print(out_)
