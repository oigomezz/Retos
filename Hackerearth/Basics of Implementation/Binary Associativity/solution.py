a = ["0 1 1 0", "0 1 1 1", "0 0 0 1", "1 1 1 1",
     "0 0 1 1", "0 0 0 0", "0 1 0 1", "1 0 0 1"]
T = int(input())

for _ in range(T):
    s = input()
    if s in a:
        print("Yes")
    else:
        print("No")
