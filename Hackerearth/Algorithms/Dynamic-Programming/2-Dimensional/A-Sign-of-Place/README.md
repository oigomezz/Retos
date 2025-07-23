# [A sign of place][link]

Bob has an array of length n whose elements lie in the range [1, n]. He compared the adjacent elements of the array and prepared a string s of length n-1 of <, >, and = signs that show the result of the comparison between the adjacent elements of the array.

Formally,

- If s[i]: <, then a[i] < a[i+1].
- If s[i]: >, then a[i] > a[i+1].
- If s[i]: =, then a[i] = a[i+1].
- For each valid index i

Unfortunately, Bob lost the array and now he wonders how many distinct arrays of length n exist such that its elements are between 1 and n. Since the count can be very large, find this count modulo 10⁹ + 7.

Two arrays are different if they differ at least one index.

## Input format

- The first line contains a number that denotes the length of the array.
- The second line contains a string s of length n-1.

## Output format

Print the number of different arrays modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/place-sign-3bb0be4c/
