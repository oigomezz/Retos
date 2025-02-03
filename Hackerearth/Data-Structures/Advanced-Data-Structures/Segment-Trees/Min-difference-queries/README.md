# [Min difference queries][link]

You have a sequence a of length n and you want to answer q queries determined by 2 integers l and r. You take all numbers present in subsequence a[l], a[l+1],..., a[r], let them be b1,b2,...,bn and number of occurrenses of each number in this subsequence be c1,c2,...,cn respectively. The answer for per query is equal to min|c[i]-c[j]| for 1 <= i < j <= t or 1 if t=1.

## Input format

- The first line contains 2 integers - n and q.
- The second line contains n numbers - a1,a2,...,an.
- Each of the next q lines contains 2 integers - ui, vi.
- You will need to answer the queries online so the information is encoded, if the answer for (i-1)th query is last (initially last=0) then the i-th query is:

- l[i] = ((ui + last) mod n) + 1
- r[i] = ((vi + last) mod n) + 1

## Output format

Output q lines, the i-th line contains the answer for the i-th query.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/min-difference-queries-f5b9c199/
