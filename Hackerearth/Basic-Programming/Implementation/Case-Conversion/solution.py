def case_conversion(s):
    a = []
    a.append(s[0].lower())
    for i in s[1:]:
        if i.isupper():
            a.append('_'+i.lower())
        else:
            a.append(i)
    return ''.join(a)


t = int(input())
for _ in range(t):
    s = input()
    out_ = case_conversion(s)
    print(out_)
