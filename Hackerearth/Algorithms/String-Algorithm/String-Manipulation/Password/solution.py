n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())
for word in words:
    if word[::-1] in words:
        ln = len(word)
        print(ln, word[ln // 2])
        break
