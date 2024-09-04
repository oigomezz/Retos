class Node:
    def __init__(self, val, hd):
        self.val = val
        self.hd = hd


def hamming_distance(a, b):
    hd = 0
    while a > 0 or b > 0:
        hd += (a & 1) ^ (b & 1)
        a >>= 1
        b >>= 1
    return hd


def solve(N, K, A):
    lst = []
    for i in range(len(A)):
        lst.append(Node(A[i], hamming_distance(A[i], K)))
    lst.sort(key=lambda x: (x.hd, x.val))
    ans = [lst[i].val for i in range(N)]
    return ans


def main():
    T = int(input())
    for _ in range(T):
        custom_input_1 = list(map(str, input().split()))
        N = int(custom_input_1[0])
        K = int(custom_input_1[1])
        A = list(map(int, input().split()))

        out_ = solve(N, K, A)
        print(' '.join(map(str, out_)))


if __name__ == "__main__":
    main()
