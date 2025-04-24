# [The maximum number][link]

You are given an array A of n elements. Let us define a function:

    F(x) = Σ Ai&x

**Note:** Here, & represents bitwise AND operator.

You are required to find the number of different values of x for which F(X) is maximized. There exists a condition for x that it must have exactly l bits sets in its binary representation.

Your task is to find a number of such values for which this function is maximized. Print the required number.

If there are infinite such numbers, then print -1.

It can be proved that under the given constraints the value to be printed is either infinite or not greater than 1e18.

## Input format

- The first line contains the number of test cases, T.
- The second line contains two space-separated integers n and l (as described in the problem).
- The third line contains n space seprated integers A1, A2, ... , An.

## Output format

There are N lines of the output. The only line of output for each test case contains a single integer as described in the problem statement.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/max-num-eb15ff4f/
