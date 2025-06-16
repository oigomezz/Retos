# [Find the Array][link]

You have two positive integer arrays A and B of same length N. But elements of array A are hidden from you. And you know A is lexicographically greater than B. You’ll be given M information about A. Each of the M information will be given in this format “i > j” or “i < j”, which means Ai is greater or smaller than Aj respectively (depending on the sign). You have to find the integers of A, or determine no such array exists. In case of multiple possible answers, find the lexicographically smallest one among them.

## Input format

- There will be multiple test cases, each input will start with an integer T, number of test cases.
- Second line will contain two integers N and M, length of the arrays and number of information about array A.
- Next line will contain N integers b1,b2,b3,...,bn - integers of array B.
- Each of the next M lines will contain an information about array A, either “i > j” or “i < j”, as described above.

## Output format

For each test case, first determine wheather it is possible to find the integers of A. If possible then first print "YES"(without qoutes) and in the second line print N integers a1,a2,a3,...,an - integers of array A. If it is impossible to find the integers, only print "NO"(without qoutes).

[link]: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/find-the-array-616201fd/
