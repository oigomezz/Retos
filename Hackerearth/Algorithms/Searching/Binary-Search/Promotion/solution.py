def is_possible(box, man, n, m, min_dist):
    tmp, tot = 0, 0
    while tot < m:
        j = 0
        while j < min_dist and tmp < n and man[tot] >= box[tmp]:
            tmp += 1
            j += 2
        tot += 1
    if tmp == n:
        return True
    return False


def dist(box, man, nb, nm):
    box.sort()
    man.sort()
    beg, end = 0, 2 * nb
    min_dist = 0
    while beg <= end:
        mid = beg + (end - beg) // 2
        if is_possible(box, man, nb, nm, mid):
            min_dist = mid
            end = mid - 1
        else:
            beg = mid + 1
    return min_dist


n_b, n_m = map(int, input().split())
box_arr = list(map(int, input().split()))
man_arr = list(map(int, input().split()))
print(dist(box_arr, man_arr, n_b, n_m))
