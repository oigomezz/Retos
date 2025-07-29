def longest_special_subseq(num, string):
    longest_len = 0
    idxes = tuple(ord(c) - 97 for c in string)  # 97 is ord('a')
    lengths = [0] * 26
    for i in idxes:
        left = max(i - num, 0)
        right = min(i + num, 25)
        length = max(lengths[left: right + 1])
        length += 1
        lengths[i] = length
        longest_len = max(longest_len, length)
    return longest_len


t = int(input())
for tc in range(t):
    n, k, s = input().split()
    n = int(n)
    k = int(k)
    print(longest_special_subseq(k, s))
