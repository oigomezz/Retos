# [Splitting Candies][link]

There is a sequence of N candies in the store. There are different types of candies, the type of the i-th candy is denoted by Ai.

Andy decided to split the sequence into continuous subarrays so that all the following conditions are satisfied

- Each candy is contained in exactly one subarray
- The size of each subarray is no more than K
- For each subarray there is at most one type of candy which is contained an odd number of times

The value of subarray AL, AL+1, ..., AR is defined as AL+AR. The value of splitting is defined as the sum of values of the subarrays.

Output the minimum possible value of splitting.

As the answer can be pretty large output it modulo 1000000007 (10⁹ + 7)

## Input format

- The first line contains N denoting the number of candies
- The second line contains an integer K denoting the maximum size of a subarray.
- Each of the next N lines contains one integer, the type of each candy.

## Output format

An integer denoting the minimum value of splitting modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/andy-and-string-operations-941f4415/
