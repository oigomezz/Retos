t = int(input())
for _ in range(t):
    s = input()
    count = 0
    length = len(s)
    tag = 0
    for i in range(length):
        if s[i] == 'a' or s[i] == 'z':
            count += (tag+1)*(length-i)
            tag = 0
        else:
            tag += 1

    print(count)
