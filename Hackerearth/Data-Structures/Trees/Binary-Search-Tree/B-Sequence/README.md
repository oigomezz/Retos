# B-Sequence

Any sequence A of size n is called B-sequence if:

- A1 < A2 < ... < Ak > Ak+1 > Ak+2 > ... > An where 1 <= k <= n. That is, a sequence which is initially strictly increasing and then strictly decreasing (the decreasing part may or may not be there).
- All elements in A except the maximum element comes atmost twice (once in increasing part and once in decreasing part) and maximum element comes exactly once.
- All elements coming in decreasing part of sequence should have come once in the increasing part of sequence.

You are given a B-sequence S and Q operations. For each operation, you are given a value val. You have to insert val in S if and only if after insertion, S still remains a B-sequence.
After each operation, print the size of S. After all the operations, print the sequence S.

Hint: Think of using some data structure to support insertion of elements in complexity better than linear.

## Input format

- First line consists of an integer N, denoting size of S.
- Second line consists of N space separated integers, denoting elements of S.
- Next line consists of an integer Q, denoting number of operations.
- Each of the following Q lines consists of an integer val.

## Output format

After each operation, print the size of S in a new line.
After all operations, print the sequence S.
