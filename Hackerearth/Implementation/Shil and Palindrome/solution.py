from collections import Counter

s = sorted(list(map(str, " ".join(input()).split())))
a = ""
m = True
d = ''

for i in Counter(s):
    if Counter(s)[i] % 2 == 0:
        a += i*(Counter(s)[i]//2)
    else:
        if m == False:
            print(-1)
            exit(0)
        else:
            if Counter(s)[i] == 1:
                d = i
            else:
                a += i*(Counter(s)[i]//2)
                d = i
            m = False

print(''.join(sorted(a)+[d]+sorted(a, reverse=True)))
