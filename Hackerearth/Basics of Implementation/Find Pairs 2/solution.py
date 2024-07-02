N, L, R = [int(x) for x in input().split()]
li = [int(x) for x in input().split()]
odd = [x for x in li if x % 2 != 0]
even = [x for x in li if x % 2 == 0]
n_odd = len(odd)
count = 0
if n_odd == 0:
    print(count)
else:
    odd.sort(reverse=True)
    even.sort(reverse=True)
    # print(odd,even)
    for k in range(n_odd):
        n_ev = len(even)
        for i in range(n_ev):
            if odd[k] + even[i] >= L and odd[k]+even[i] <= R:
                count += (n_odd - k) * (n_ev - i)
                even = even[:i]
                break
    print(count)
