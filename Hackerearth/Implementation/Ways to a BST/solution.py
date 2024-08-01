# This code is a Python translation of a C++ program that deals with binary trees and combinatorial counting.

class Node:
    def __init__(self, value):
        self.value = value
        self.total = 0
        self.left_child = None
        self.right_child = None


maxN = 1000
MOD = int(1e9 + 7)
fact = [0] * (maxN + 1)


def initialize_node(value):
    return Node(value)


def multiply_mod(a, b):
    return ((a % MOD) * (b % MOD)) % MOD


def insert(root, value):
    if root is None:
        return initialize_node(value)
    if value <= root.value:
        root.left_child = insert(root.left_child, value)
    else:
        root.right_child = insert(root.right_child, value)
    return root


def update(root):
    if root is None:
        return 0
    root.total = 1 + update(root.left_child) + update(root.right_child)
    return root.total


def power(a, b):
    if b == 0:
        return 1
    result = power(multiply_mod(a, a), b // 2) % MOD
    if b % 2:
        result = multiply_mod(a, result)
    return result


def get_inverse(a):
    return power(a, MOD - 2)


def get_count(root):
    if root is None:
        return 1
    left_count = get_count(root.left_child)
    right_count = get_count(root.right_child)
    x = 0 if root.left_child is None else root.left_child.total
    y = 0 if root.right_child is None else root.right_child.total
    answer = multiply_mod(multiply_mod(get_inverse(fact[x]), get_inverse(
        fact[y])), multiply_mod(left_count, right_count))
    answer = multiply_mod(answer, fact[x + y])
    return answer


def preprocess():
    fact[0] = 1
    for i in range(1, maxN + 1):
        fact[i] = multiply_mod(i, fact[i - 1])


def main():
    preprocess()
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = 0
        root = None
        for _ in range(n):
            a = int(input())
            root = insert(root, a)
        update(root)
        answer = get_count(root)
        print(answer)


if __name__ == "__main__":
    main()
