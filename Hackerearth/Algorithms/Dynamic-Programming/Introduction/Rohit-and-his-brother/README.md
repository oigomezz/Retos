# [Rohit and his brother][link]

Rohit and his brother Rohan have two old wooden chests, A and B, consisting of N integers. They also got an old rusted trunk with lots of diamonds inside it. However, the rusted trunk has a lock that can only be opened if they know the number of combinations possible such that the following conditions are satisfied.

Assume they choose a set of numbers {S1,S2,S3 ... Sk} consisting of integers from 1 to N. Let Amax denote the maximum element of the numbers, {A[S1], A[S2], ..., A[Sk]} and Bsum denote the sum of the elements {B[S1], B[S2], ..., B[Sk]}. Then, Amax must be greater than or equal to Bsum. Since the answer could be large, compute it modulo 10⁹ + 7.

## Input format

- The first line contains a single integer T representing the number of test cases. Then each test case follows.
- The first line of each test case contains an integer N denoting the number of integers in the wooden trunks A and B.
- The second line of every test case contains N integers denoting the integers contained in the wooden chest A.
- The third line of every test case contains N integers denoting the integers contained in the wooden chest B.

## Output format

For each test case, print an integer denoting the number of subsets or combinations satisfying the conditions given in the statement modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/rohit-and-his-brother-7fa500c4/
