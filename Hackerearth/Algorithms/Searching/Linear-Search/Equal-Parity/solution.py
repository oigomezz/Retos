test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    a = map(int, input().split())
    even_elements = [el for el in a if el % 2 == 0]
    evens = len(even_elements)
    odds = 2 * n - evens
    if evens >= odds:
        print("YES")
    elif sum((n & (~ (n - 1))) // 4 for n in even_elements) >= (n - evens):
        print("YES")
    else:
        print("NO")
