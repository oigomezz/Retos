n = int(input())
s = input()
s2 = s.replace("w", "vv")
s1 = s2.replace("vv", "w")
l = [len(s1), len(s2)]
print(*l)
