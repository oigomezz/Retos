# [Bob And The Magic Count][link]

Bob is a brilliant student in the class and hence his teacher assigned him a problem. He has been given an array A of N positive integers and has been asked to make the magic count of the whole array equal to 1 by performing the below operation some number of times. The magic count of the array is the greatest common divisor (GCD) of all numbers in it.

- In one operation Bob is allowed to choose some integer i (1 <= i <= N) and replace A[i] with GCD(A[i], i) the cost of this operation is N - i + 1. The total cost will be the sum of the costs of all the performed operations.

Help Bob in finding the minimum total cost to make the magic count of all the whole array equal to 1.

**Note:** Consider 1-based array indexing for the above problem.

## Input format

- The first line contains a single integer T, denoting the number of test cases.
- The first line of each test case contain the integer N, denoting the number of elements in the array A.
- The second line of each test case contains N space-separated integers, denoting the elements of the array A.

## Output format

For each test case, print the minimum total cost to make the magic count of the whole array equal to 1.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/bob-and-the-magic-count-d016bec6/
