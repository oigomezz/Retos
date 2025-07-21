n = int(input())
v = list(map(int, input().split()))
freq = [False] * 1024

for ele in v:
    for i in range(1024):
        if freq[i]:
            freq[i ^ ele] = True
    freq[ele] = True
    c = sum(freq)
    print(c, end=' ')
print()
