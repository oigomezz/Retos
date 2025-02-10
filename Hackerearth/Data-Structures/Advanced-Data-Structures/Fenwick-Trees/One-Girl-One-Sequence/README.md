# One Girl One Sequence

You are given a sequence of distinct integers a1,a2,...,an and an integer x and you have to perform the following operations:

1. Remove the current minimum from a. This operation costs x.
2. Remove the current maximum from a. This operation costs the number of elements located on the right to the maximum. Formally, if the maximum is a[i] and the current size of the sequence is k, then the cost will be k-i.

What is the minimum cost to erase the whole sequence?

## Input format

- First line: Two integers n and x denoting the size of the sequence and the cost of the first type of operation.
- Second line: A sequence a1,a2,...,an.
- It is guaranteed that all elements of a are distinct.

## Output format

Print an integer denoting the minimum cost to erase the whole sequence.
