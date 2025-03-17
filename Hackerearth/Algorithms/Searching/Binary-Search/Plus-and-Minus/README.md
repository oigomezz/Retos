# [Plus and Minus][link]

Initially, you have an array of length 2, which is a = [a1, a2]. Here a1 >= a2 >= 0.

In each step, you must choose the two largest integers ai and aj in the array, where ai >= aj, and insert two integers ai + aj and ai - aj to the array (in any positions).

Thus, you can construct an array of any even length >= 4.

Now you are given an array of even length N.

Please determine whether you can form this array by the steps. If so, then find out which is the initial array.

## Input format

- The first line contains a single integer T, the number of test cases.
- For each testcase:
  - The first line contains one odd integer N, the length of the arrays.
  - The second line contains N positive integers a1, a2, ..., an.
- The sum of N over all test cases does not exceed 10⁷.

## Output format

- For each testcase, output "YES" if you can construct the given array by the steps. Otherwise, output "NO".

- If you can construct such an array, then print two integers a1, a2. Note that a1 >= a2.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/plus-and-minus-0f3ab24f/
