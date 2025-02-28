class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create(data):
    return Node(data)


def insert(root, data):
    if data > root.data:
        if root.right is None:
            root.right = create(data)
        else:
            insert(root.right, data)
    else:
        if root.left is None:
            root.left = create(data)
        else:
            insert(root.left, data)


def find_common_root(root, x, y):
    if x > root.data and y > root.data:
        return find_common_root(root.right, x, y)
    elif x < root.data and y < root.data:
        return find_common_root(root.left, x, y)
    else:
        return root


def find_max(parent, x, current_max):
    if current_max < parent.data:
        current_max = parent.data
    if x == parent.data:
        return current_max
    elif x > parent.data:
        return find_max(parent.right, x, current_max)
    else:
        return find_max(parent.left, x, current_max)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    root = create(data[0])
    for i in range(1, n):
        insert(root, data[i])
    x, y = map(int, input().split())
    parent = find_common_root(root, x, y)
    max1 = find_max(parent, x, 0)
    max2 = find_max(parent, y, 0)
    print(max(max1, max2))


if __name__ == "__main__":
    main()
