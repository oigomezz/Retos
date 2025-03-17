# [Endless Integer Sequence][link]

You have an infinite sequence of natural numbers as follows 1,2,3,4,5,...

You need to perform these 2 types of queries on this infinite sequence,

- Query 1

  - Delete an integer X from this infinite sequence.
  - After deleting the element, the remaining sequence is concatenated together.

- Query 2
  - Find the K smallest integer in this infinite sequence.

**NOTE:** In Query 1, for the element to be deleted, it is provided that X will be present in the sequence at the time of query.

## Input format

- First line contains an integer Q, the number of queries.
- Next Q lines contain 2 space separated integers denoting each query as follows,

  - 1 X: Query 1, with parameter X the integer to be deleted.
  - 2 K: Query 2, with parameter K to find K-th smallest element in the infinite sequence.

## Output format

For each Query of type 2, output a single integer denoting the K-th smallest element in the infinite integer sequence.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/endless-integer-sequence-088184af/
