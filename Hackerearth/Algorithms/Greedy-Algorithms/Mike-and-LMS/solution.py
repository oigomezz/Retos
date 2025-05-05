n = int(input())
s = input().strip()
substring = ''
for i in range(n):
    substring = max(substring, s[i:])

print(substring)
