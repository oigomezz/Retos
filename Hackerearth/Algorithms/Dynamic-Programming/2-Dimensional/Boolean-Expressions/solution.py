s, o = input().split()
n = len(s)
f = [[[0] * 310 for _ in range(310)] for _ in range(2)]

for i in range(n):
    f[int(s[i])][i][i] = 1

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            for c in range(2):
                for d in range(2):
                    if o[k] == 'a':
                        x = c & d
                    elif o[k] == 'x':
                        x = c ^ d
                    else:
                        x = c | d
                    inc = f[c][i][k] * f[d][k + 1][j] % 1000000009
                    f[x][i][j] = (f[x][i][j] + inc) % 1000000009

q = int(input())
output = []
for _ in range(q):
    line = list(map(str, input().split()))
    l = int(line[0])
    r = int(line[1])
    op = line[2]
    x = 1 if op[0] == 't' else 0
    output.append(f[x][l - 1][r - 1])

print(*output, sep='\n')
