def solve(n, start, finish, ticket_cost):
    if start == finish:
        return 0
    left, right = sorted((start, finish))
    path_1_cost = sum(ticket_cost[(left - 1): (right - 1)])
    path_2_cost = sum(ticket_cost) - path_1_cost
    return min(path_1_cost, path_2_cost)


N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, Ticket_cost)
print(out_)
