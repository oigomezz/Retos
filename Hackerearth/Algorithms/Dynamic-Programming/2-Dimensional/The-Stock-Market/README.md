# [The stock market][link]

You are given an array A consisting of N integers and a special number K. You have to divide the array into K non-empty subarrays. The sum of elements of the 1st, 3rd, 5th, 7th...(odd) subarrays is the price at which you buy the stocks and the sum of elements of the 2nd, 4th, 6th, 8th....(even) subarrays is the price at which you sell the stocks. The profit of this transaction would be equal to = selling price - buying price, where the selling price is the sum of elements of the even indexed subarrays and the buying price is the sum of elements of the odd indexed subarrays.

**Task:** Determine the maximum profit you can make by buying and selling the stocks in an optimal manner.

## Input format

- The first line contains T denoting the number of test cases. T also specifies the number of times you have to run the solve function on a different set of inputs.
- For each test case:
  - The first line contains a single integer N denoting the size of the array A.
  - The second line contains N space-separated integers denoting the elements of the array A.
  - The third line contains the special number K.

## Output format

For each test case in a new line, print a single integer representing the maximum profit.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/the-stock-market-f51a84fd/
