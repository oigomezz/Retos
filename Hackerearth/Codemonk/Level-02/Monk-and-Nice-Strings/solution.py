n = int(input())
se = []
for i in range(1, n + 1):
    s = input()
    k = sum(1 for item in se if item < s)
    print(k)
    se.append(s)
    se.sort()
