t = int(input())
for _ in range(t):
    n = int(input())
    p, w = map(int, input().split())
    num_of_emp = list(map(int, input().split()))
    desired_floor = [0] * (n+1)
    persons = [0] * (n+1)
    current_w = 0
    current_p = 0
    ans = n
    for i in range(n-1):
        floors = list(map(int, input().split()))
        weights = list(map(int, input().split()))
        for j in range(len(weights)):
            desired_floor[floors[j-1]-1] += weights[j-1]
            persons[floors[j-1]-1] += 1
            current_w += weights[j-1]
            current_p += 1
        current_w -= desired_floor[i]
        current_p -= persons[i]
        if current_w > w and ans == n:
            ans = i+1
        if current_p > p and ans == n:
            ans = i+1
    print(ans)
