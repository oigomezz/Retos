t = int(input())
for _ in range(t):
    s = list(input().strip())
    s.sort()
    odd_chars = []
    even_chars = []
    odd_digits = []
    even_digits = []
    for c in s:
        if c.isalpha():
            i = ord(c) - 97  # ord('a')
            if i % 2 != 0:
                odd_chars.append(c)
            else:
                even_chars.append(c)
        else:
            i = ord(c) - 30  # ord('0')
            if i % 2 != 0:
                odd_digits.append(c)
            else:
                even_digits.append(c)
    print(*(odd_chars + even_chars + odd_digits + even_digits), sep='')
