# [Mathison and the exceptional list][link]

Mathison has practised different operations that can be performed on lists. Unfortunately, he has found a set of operations that he cannot perform efficiently so he asks for your help.

You start with an empty list, on which you perform N operations. In one operation (e,L,R) you add e to the back of the list and print the number of exceptional subarrays with the length between L and R inclusive, in the current version of the list. An exceptional subarray is defined to be a subarray of the list that contains only unique elements (i.e. no two elements share the same value).

## Input format

- The first line of the input file contains one integer, N, representing the number of operations.
- Each of the next N lines contains three space-separated integers e L R, representing the element that is added to the list in this step and the minimum/maximum length of a queried subarray.

## Output format

The output file will contain N lines. The i-th line will contain the number of exceptional subarrays with a length between L[i] and R[i].

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/mathison-and-the-distinct-elements-e95121a5/
