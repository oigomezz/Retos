# [Array and good pairs][link]

You are given an array A of length N. A pair (a,b) is considered good if the following criterion is fulfilled:

Consider the decimal representation of a and b. a has digits a1, a2, ..., ak and b has digits b1, b2, ..., bk. (a,b) is good only if there is no index y (1 <= y <= k) such that ay and by are non-zero elements.

You are required to process Q queries where each having one of the following forms:

- 0 i x: Change the i-th index to x in the array.
- 1 l r: Consider all the pairs (i,j) such that l <= i <= j <= r such that (ai, aj) is a good pair and ai ∏ aj add to the answer.

**Note:** As the answer can be large, print answer modulo 10⁹ + 7.

## Input format

- First line: An integer N (1 <= N <= 10⁵) representing the length of the array.
- Second line: N space-separated integers that representing the elements of the array (0 <= Ai <= 999999)
- Next q lines: One of the queries of the following forms:
  - 0 i x
  - 1 l r

## Output format

For each query of type 1, print the required answer in a separate line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/array-and-good-pairs-7f649027/
