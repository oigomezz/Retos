# [Killjee and subsets][link]

Killjee is playing with an array a, which has n integers. He is trying to encrypt this array as a single integer.

Let l be the largest number in array a. Then, the code for array a is Σ bj \* 31^(i) mod 10⁹ + 7.

Here, bj is the size of largest subset of array a whose XOR is equal to j.If there exist no subset of array a whose XOR is j then bj = 0.

## Input format

- First line of input contains a single integer n.
- Next line contains n space separated integers, elements of array a.

## Output format

Print a single integer code of the array a.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/killjee-and-subsets-43a47e0b/
