# [Binomial Sum of Products][link]

A function f(x,y) is defined as f(x,y) = (x y) if x >= y else x\*y where (x y) = x! / (y!(x-y)!)

There will be total q queries and each query will have four integers i.e. a, b, c and d. You need to compute the value of Σ Π f(i,j) for every query.

As the output number can be very large. So, you need to print answer modulo 10⁹ + 7.

## Input format

- First line will have a single integer denoting the value of q.
- Each line in next q lines will have four space separated integers denoting the value of a,b,c and d.

## Output format

Output q lines, where i-th line denoting the answer represents the answer of the i-th query modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/binomial-sum-of-products-caff260f/
