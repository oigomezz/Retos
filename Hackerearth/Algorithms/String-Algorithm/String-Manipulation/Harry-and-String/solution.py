t = int(input())
for _ in range(t):
    s = input().strip()
    a = [c for c in s if c in 'aeiou']
    b = sorted(a)
    if a == b:
        print("Good")
    elif a == b[::-1]:
        print("Worst")
    else:
        print("Bad")
