# Special Subarrays

An array is said to be special, if we can break it down into subarrays where every subarray (length > 1) starts and ends with 0 and rest all other numbers are 1.

Given N binary arrays.

Sam decided to write down all the distinct prefix subarrays of the given N binary arrays on a paper (he'll write distinct prefix only). After that he counts the number of special subarrays in every prefix and sum that up (a special subarray will be counted as many times as it is contained in each prefix).

Find the sum found by Sam modulo 10⁹ + 7.

## Input format

- The first line contains N denoting the number of binary arrays.
- The ith of the next N lines contains the binary array in form of a string S[i].

## Output format

Sum found by Sam modulo 10⁹ + 7.
