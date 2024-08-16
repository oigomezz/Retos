from collections import Counter

n = int(input())
m = int(input())
rna = input()
rna_counter = dict(Counter(rna))
guanine = 'G'
cytosine = 'C'
best = 0
vaccine_number = 0

for _ in range(n):
    l = int(input())
    s = input()
    s_counter = dict(Counter(s))
    status = s_counter.get(cytosine, 0) * rna_counter.get(guanine, 0) + s_counter.get(guanine, 0) * rna_counter.get(cytosine, 0)
    if status > best:
        best = status
        vaccine_number = _ + 1
        
print(vaccine_number)
