from collections import deque


test_cases = int(input())
for _ in range(test_cases):
    n, m, budget_limit = map(int, input().split())
    adjacency_list = [[] for _ in range(601)]
    dp = [[(1 << 60) - 1 for _ in range(2001)] for _ in range(601)]

    for _ in range(m):
        a, b, c, d = map(int, input().split())
        adjacency_list[a].append((b, (c, d)))

    queue = deque()
    queue.append((1, 0, 0))  # (node, cost, distance)
    dp[1][0] = 0

    while queue:
        current_node, current_cost, current_distance = queue.popleft()
        for neighbor in adjacency_list[current_node]:
            neighbor_node, (cost_to_neighbor,
                            distance_to_neighbor) = neighbor
            if cost_to_neighbor + current_cost > budget_limit:
                continue
            dp[neighbor_node][cost_to_neighbor + current_cost] = min(
                dp[neighbor_node][cost_to_neighbor + current_cost], dp[neighbor_node][cost_to_neighbor + current_cost - 1])
            if dp[current_node][current_cost] + distance_to_neighbor < dp[neighbor_node][cost_to_neighbor + current_cost]:
                dp[neighbor_node][cost_to_neighbor +
                                  current_cost] = dp[current_node][current_cost] + distance_to_neighbor
                queue.append((neighbor_node, cost_to_neighbor + current_cost,
                              dp[neighbor_node][cost_to_neighbor + current_cost]))

    for i in range(1, n + 1):
        for c in range(1, budget_limit + 1):
            dp[i][c] = min(dp[i][c], dp[i][c - 1])

    query_count = int(input())

    for _ in range(query_count):
        destination, budget = map(int, input().split())
        print(-1 if dp[destination][budget] ==
              (1 << 60) - 1 else dp[destination][budget])
