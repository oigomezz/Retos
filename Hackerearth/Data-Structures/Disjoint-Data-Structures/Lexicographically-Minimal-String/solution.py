def solution(a, c, b):
    # ord('a') = 97
    code = 97
    roots = list(range(26))

    def find(x, parents):
        while x != parents[x]:
            x = parents[x]
        return x

    def join(x, y, parents):
        x = ord(x) - code
        y = ord(y) - code
        px = find(x, parents)
        py = find(y, parents)
        if px < py:
            parents[py] = px
        elif px > py:
            parents[px] = py

    for i in range(len(a)):
        join(a[i], b[i], roots)
    res = ''
    for c in c:
        root = find(ord(c) - code, roots)
        res += chr(root + code)
    return res


A = input()
B = input()
C = input()

out_ = solution(A, C, B)
print(out_)
