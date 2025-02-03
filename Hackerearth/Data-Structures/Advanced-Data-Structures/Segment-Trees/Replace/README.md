# [Replace][link]

Yet another interesting problem about queries!

You have an array of n integers and q queries on this array. There are two types of queries:

1. 1 ai bi xi yi - change all occurrences of xi to yi on the segment [ai,bi]
2. 2 ai bi xi - count number of occurrences of xi on the segment [ai,bi]

This problem will be very popular! So you should solve it before before it became mainstream.

## Input format

- The first line of input contains two space separated integers n and q - size of array and number of queries.
- The second line of input contains n space separated integers a1,a2,...,an- the elements of the array before queries.
- Then q lines follow. The i-th of them contains parameters of the i-th query. The i-th line can be:
  - 1 ai bi xi yi - parameters for first type query or
  - 2 1 ai bi xi - parameters for second type query

## Output format

For each query of second type print number of occurrences of xi on the segment [ai,bi].

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/replace-27c5286c/
