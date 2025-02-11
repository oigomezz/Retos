# [Buy 'Em All][link]

Alice went shopping with her Dad to a magical shop.

She wants to buy some golden snitches from the shop. All the snitches in the shop are kept on a rack in straight line, one kept aside the other.

Shop being magical, doesn't let anyone pick snitch from any arbitrary position. If someone want to buy more than one snitch one can only pick contiguous segment of the items. And the cost of the segment is determined by the cost of each item in it. Alternatively Cost of segment from position l to r(inclusive) is.

- Cost = C[l] \* C[l+1] + C[l+2] \* C[l+3] + ... + C[r-1] \* C[r] if length of segment is even.
- Cost = C[l] \* C[l+1] + C[l+2] \* C[l+3] + ... + C[r-1] \* 1 otherwise.

where C[1],C[2],...,C[n] are the cost of each item from 1 to n.

Alice's Dad has exactly k Rupees(Currency in India) and he wants to spend it all on Alice. Help Alice find the number of segments which she can afford to buy with k Rupees.

**Note:** Word "item" and "snitch" are used interchangeably in the above statements.

## Input format

- First line contains n and k denoting number of snitches in shop and the amount of money Alice's Dad has.
- Second line contains n space separated integers C1, C2, ..... Cn denoting cost of each snitch present in the shop.

## Output format

Output a single number as asked in the question.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/buy-em-all-d972d5c9/
