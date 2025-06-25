def can_you_count(s):
    vowels = 'aeiou'
    t = ''
    total = 1
    for c in s:
        if c in vowels:
            if c not in t:
                t += c
        elif c == '_':
            total *= len(t)
    return total % 9223372036854775808


T = int(input())
for _ in range(T):
    s = input()

    out_ = can_you_count(s)
    print(out_)
