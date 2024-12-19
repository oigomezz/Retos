a = ["0 1 1 0", "0 1 1 1", "0 0 0 1", "1 1 1 1",
     "0 0 1 1", "0 0 0 0", "0 1 0 1", "1 0 0 1"]
t = int(input())
for _ in range(t):
    s = input()
    if s in a:
        print("Yes")
    else:
        print("No")
