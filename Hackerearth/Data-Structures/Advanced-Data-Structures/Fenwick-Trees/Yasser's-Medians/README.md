# [Yasser's Medians][link]

Given N numbers and an integer K find:

    (N^(maxmed)) mod 1e9 + 7

Formally: we can define maxmed as the maximum median of each subarray of length K.

Note that: the median of K numbers indexed from 1 is ((k+1)/2)-th smallest of them, rounding down for even K.

## Input format

- The first line contains two integers N and K denoting the number of elements and size of the subarray.
- The second line contains N space-separated integers.

## Output format

Print the answer as described above.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/yassers-medians-b625cdde/
