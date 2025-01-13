# [Supreme Subset][link]

Given a multiset of integers having cardinality n, find its Supreme Subset.

A supreme subset of a given multiset is one of its subsets in which -

1. if any two elements i,j are chosen from subset, |i-j| is divisible by m, where x represents absolute value of x.
2. it has the highest cardinality/size among all candidate subsets satisfying condition 1.
3. If there are multiple subsets satisfying above 2 conditions, the supreme subset is the one which is smallest by set comparison.

Finding order by set comparison - Given two sets of the same size, the smaller one is defined to be the one which is lexicographically smaller when both sets are arranged in non-decreasing order, for example, the set {3,2,1} is smaller than {3,2,2}.

## Input format

- The first line of the input contains 2 integers, n,m as specified in the problem statement.
- The second line contains n integers, representing the multiset A.

## Output format

First line should have 1 integer, k, representing cardinality of the Supreme Subset.
Second line should have k members of the supreme subset in sorted order.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/supreme-subset-bb866a75/
