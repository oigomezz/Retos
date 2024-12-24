from collections import defaultdict

t = int(input())
for _ in range(t):
    str_input = input()
    A = defaultdict(int)

    for char in str_input:
        A[char] += 1

    count = 0
    for char in str_input:
        if A[char] != 0:
            count += 1
            A[char] = 0

    if count % 2 == 0:
        print("Player2")
    else:
        print("Player1")
