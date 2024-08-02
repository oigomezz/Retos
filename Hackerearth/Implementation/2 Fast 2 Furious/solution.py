n = int(input())
dom = list(map(int, input().split()))
brian = list(map(int, input().split()))
diff = 0
a = 0
c = 0
new_a, new_c = 0, 0
for i in range(n-1):
    a = abs(brian[i+1]-brian[i])
    c = abs(dom[i+1]-dom[i])
    if new_a < a:
        new_a = a
    if new_c < c:
        new_c = c
if new_a < new_c:
    print("Dom")
    print(new_c)
elif new_c < new_a:
    print("Brian")
    print(new_a)
else:
    print("Tie")
