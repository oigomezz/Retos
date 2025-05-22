def find(node):
    if node == disjoint_set_union[node]:
        return node
    disjoint_set_union[node] = find(disjoint_set_union[node])
    return disjoint_set_union[node]


def union(node_a, node_b):
    root_a = find(node_a)
    root_b = find(node_b)
    if root_a == root_b:
        return False
    disjoint_set_union[root_a] = root_b
    minimum_values[root_b] = min(
        minimum_values[root_b], minimum_values[root_a])
    return True


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        node_count = int(input())
        edge_count = int(input())

        global disjoint_set_union, minimum_values
        disjoint_set_union = list(range(node_count))
        minimum_values = []

        node_values = list(map(int, input().split()))
        minimum_values.extend(node_values)

        edges = []
        for _ in range(edge_count):
            edge_data = list(map(int, input().split()))
            edges.append((edge_data[2], edge_data[0] - 1, edge_data[1] - 1))

        edges.sort()
        total_weight = 0
        for weight, node_x, node_y in edges:
            if union(node_x, node_y):
                total_weight += weight

        minimum_in_tree = float('inf')
        for i in range(node_count):
            if disjoint_set_union[i] == i:
                minimum_in_tree = min(minimum_in_tree, minimum_values[i])
                total_weight += minimum_values[i]

        total_weight -= minimum_in_tree
        print(total_weight)
