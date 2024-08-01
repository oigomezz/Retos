t = int(input())
for _ in range(t):
    s = list(input())
    count = 0
    for i in range(len(s)):
        if s[i] == "B":
            if i - 2 >= 0 and s[i-2] == "W":
                s[i-2] = "_"
                count += 1
            if i - 1 >= 0 and s[i-1] == "W":
                s[i-1] = "_"
                count += 1
            if i+1 < len(s) and s[i+1] == "W":
                s[i+1] = "_"
                count += 1
            if i+2 < len(s) and s[i+2] == "W":
                s[i+2] = "_"
                count += 1
    print(count)
