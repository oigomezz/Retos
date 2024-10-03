# Array Construction

You are given two arrays a = [a1,a1,...,an] and b = [b1,b2,...,bn], with a1 = a2 = ... = an = 0.

First, you must choose two of indices i,j (1 <= i,j <= m, i != j) and assign ai = aj = 1.

Then perform the following operation as many times as you want:

- Choose an index k (1<=k<=n), and add the product of the two largest integers in a to ak. That is, ak = ak + ai \* aj, where ai >= aj >= al for all l (1<=l<=n, l!=i, l!=j).

Now, determine if you can transform the array a into the array b or not.

If you can construct the array, then print “YES”. Otherwise, print “NO”.

## Input format

- The first line contains a single integer T — the number of test cases.
- For each testcase:
  - The first line contains one integer n — the length of the arrays.
  - The second line contains n nonnegative integers b1,b2,...,bn.
- The sum of n over all test cases does not exceed 10⁶.

## Output format

For each Testcase, output "YES" if the array a can be transformed into b. Otherwise, output "NO".
