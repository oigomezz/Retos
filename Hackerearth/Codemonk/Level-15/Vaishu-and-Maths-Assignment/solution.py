from functools import lru_cache

x = 0
y = 0
num = None
n = 0
answer_set = set()


@lru_cache(maxsize=None)
def calculate(idx, tar):
    if tar < x or tar > y:
        return None

    if idx >= n:
        return tar

    num_val = num[idx]

    ans1 = calculate(idx+1, tar-num_val)
    answer_set.add(ans1)

    ans2 = calculate(idx+1, tar+num_val)
    answer_set.add(ans2)


lnxy = list(map(int, input().split()))
l = lnxy[0]
n = lnxy[1]
x = lnxy[2]
y = lnxy[3]

num = list(map(int, input().split()))

calculate(0, l)

queries = int(input())
for _ in range(queries):
    input_arg = list(input().split())
    sign = input_arg[0]
    val = int(input_arg[1])

    if sign == ">":
        found = False
        for item in answer_set:
            if item != None and item > val:
                found = True
                break
        if found:
            print("YES")
        else:
            print("NO")
    else:
        found = False
        for item in answer_set:
            if item != None and item < val:
                found = True
                break
        if found:
            print("YES")
        else:
            print("NO")
