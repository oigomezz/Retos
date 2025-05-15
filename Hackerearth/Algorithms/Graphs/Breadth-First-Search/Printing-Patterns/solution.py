r, c, ci, cj = map(int, input().strip().split())
pattern = []
for i in range(r):
    row = []
    for j in range(c):
        vertical = abs(i - ci)
        horizontal = abs(j - cj)
        row.append(max(vertical, horizontal))
    pattern.append(row)

for row in pattern:
    print(*row)
