T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    set_s = list(set(s))
    reduce_op = 0
    for i in range(len(set_s)):
        reduce_op += s.count(set_s[i])//2
    print(reduce_op)
