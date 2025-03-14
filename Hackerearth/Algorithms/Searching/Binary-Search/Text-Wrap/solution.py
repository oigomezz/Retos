def check(w):
    prevw = 0
    line = 0
    first = True
    for el in arr:
        if el > w:
            return False
        if prevw + int(not first) + el <= w:
            prevw += el + int(not first)
        else:
            line += 1
            prevw = el
        first = False
    return line + int(prevw > 0) <= m


n, m = map(int, input().split())
arr = list(map(int, input().split()))
end = 1
while not check(end):
    end *= 2

beg = end // 2
res = end

while beg <= end:
    mid = (beg + end) // 2
    if check(mid):
        res = mid
        end = mid - 1
    else:
        beg = mid + 1

print(res)
