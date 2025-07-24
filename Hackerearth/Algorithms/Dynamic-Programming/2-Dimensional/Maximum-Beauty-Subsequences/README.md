# [Maximum beauty subsequences][link]

A string is said to contain a value that is known as its beauty.

You are given M pairings where the i-th pairing is {(ai,bi) : Ki}. Here, ai and bi are lowercase English letters and Ki is a positive integer.

There exists a string S of length L. For the i-th pairing, let the number of indices j ∈ [1, L-1] such that Sj = ai and Sj+1 = bi be counti. The beauty of S is the sum of counti \* Ki for each i ∈ [1, M].

You are given a string A of length N consisting of lowercase English letters. A string can be formed from a subsequence of a string by concatenating the characters of the subsequence in order of occurrence. You are required to find the maximum beauty that can be obtained by selecting any strings that can be formed by a subsequence of A.

## Input format

- The first line contains a single integer N that denotes the length of string A.
- The second line contains string A.
- The third line contains a single integer M which denotes the number of pairings.
- The next M lines represent the pairings. Each of these lines contain three space-separated values. The first two are the lowercase English letters ai and bi. The third value is the integer ki.

## Output format

Print a single line containing the maximum beauty that can be obtained from a string formed by a subsequence of A.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/maximum-beauty-subsequence-764b18e3/
