from functools import lru_cache

happy = set(el for el in [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30])
pri = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
n = int(input())
arr = list(map(int, input().split()))
num = []
count = [0]*(31)
for el in arr:
    if el in happy:
        num.append(el)
        count[el] += 1

n = 31
mod = 10**9+7


@lru_cache(None)
def helper(ind, mask, t):
    if ind == n:
        return 1 if t else 0
    else:
        temp = 0
        ans = helper(ind+1, mask, t)
        if ind == 1:
            ans += ((pow(2, count[1], mod)-1+mod) %
                    mod)*helper(ind+1, mask, True)
            ans %= mod
            return ans

        for i in range(len(pri)):
            if ind % pri[i] == 0:
                temp += 1 << i

        if temp & mask:
            return ans
        else:
            ans += (count[ind]*helper(ind+1, mask | temp, True))
            ans %= mod
            return ans


res = helper(1, 0, False)
print(res)
