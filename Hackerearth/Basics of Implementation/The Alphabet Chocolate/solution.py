t = int(input())
while t > 0:
    s = input()
    print(sum([(i+1)*(len(s)-i)
          for i in range(len(s))if (s[i].lower() in "aeiou")]))
    t -= 1
