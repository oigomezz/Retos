# [Recursive Sums][link]

Little Bear has received a home assignment to find the sum of all digits in a number N. Following his affinity towards single digit number, he intends to repeatedly compute the sum of all digits until the sum itself becomes a single digit number.

Can you write a program to compute the final single-digit sum?

As the number N is very big, it is given in the following run length encoded format - N is represented as a sequence of M blocks, where each block i (0 ≤ i < M) is represented by two integers - (len[i], d[i]). This implies that the digit d[i] occurs len[i] number of times.

For example, {(2,1), (1,2), (2,9)} represents the number 11299.

## Input format

- The first line contains a single integer T, denoting the number of test cases.
- Each test case starts with a single integer M, which is the number of following run-length encoded blocks.
- Each of the next M lines contains two space separated integers: len[i] and d[i].

## Output format

Print the single-digit sum for each of the T test cases in a new line.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/recursive-sums/
