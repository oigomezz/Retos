# [XOR queries][link]

You are given a 1indexed array A, of length n, and q queries to be performed on it. The queries are of two types

- 1 i x : Change the value of A[i] to x.
- 2 L R I J : Find l,r,i and j according to the code below. Consider the subarray B = [A[l], A[l+1], ..., A[r]]. Sort B, and find the Bitwise xor of B[i], B[i+1], ..., B[j] in the sorted array B.

You maintain the answer to the last query of type 2 in variable ans . Note that ans is initially 0. Now, whenever you get a query of type 2, calculate l,r,i and j as:

    l = 1 + ((ans ^ L) % n);
    r = 1 + ((ans ^ R) % n);
    if(l > r) swap(l, r);
    i = 1 + ((I ^ ans) % (r - l + 1));
    j = 1 + ((J ^ ans) % (r - l + 1));
    if(i > j) swap(i, j);

Here ^ denotes the bitwise xor operator, and % denotes the modulo operator

Note that array A is NOT changed in a query of second type.

## Input format

- The first line contains n and q
- The next line contains n space separated integers representing the array A
- Each of the next q lines contain a query either of type 1 or type 2 .

## Output format

For each of the query of type 2, print the required value on a new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/xor-queries-1/
