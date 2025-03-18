def comp(customers, items, mid, d):
    i, j = 0, mid
    while j >= 0:
        d -= max(0, items[i] - customers[j])
        if d < 0:
            return False

        j -= 1
        i += 1

    return True


n, m, d = [int(x) for x in input().split()]
customers = [int(x) for x in input().split()]
items = [int(x) for x in input().split()]

customers.sort(reverse=True)
items.sort()
left, right = 0, min(n, m) - 1
while left <= right:
    mid = left + (right - left)//2
    if comp(customers, items, mid, d):
        left = mid + 1
    else:
        right = mid - 1

i, j = 0, right
customer_used = 0
while j >= 0:
    d -= max(0, items[i] - customers[j])
    customer_used += min(customers[j], items[i])
    j -= 1
    i += 1

customer_used -= d
if customer_used < 0:
    customer_used = 0

print(f'{right+1} {customer_used}')
