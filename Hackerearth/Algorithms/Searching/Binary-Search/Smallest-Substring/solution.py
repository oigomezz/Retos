from collections import defaultdict


def smallest_sub_string(str):
    n = len(str)
    if n == 0 or n == 1:
        print(n)
    else:
        freq = defaultdict(int)
        max_char = len(set(str))
        min_len = n + 1
        start = 0
        for i in range(n):
            freq[str[i]] += 1
            if len(freq) == max_char:
                while start < i and freq[str[start]] > 1:
                    freq[str[start]] -= 1
                    start += 1
                curr_len = i - start + 1
                min_len = min(min_len, curr_len)
        return min_len


S = input()
out_ = smallest_sub_string(S)
print(out_)
