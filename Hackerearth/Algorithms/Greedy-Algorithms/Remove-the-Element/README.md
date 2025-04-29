# [Remove the element][link]

You are given an integer array A of size N. You can perform an operation exactly N number of times. In the operation, you can remove one element from the array A and the operation will cost Ai units if i-th is removed from the array. The operation will take 1 second.

Elements of array A will keep on increasing every second until it is removed. Let i-th element is Ai at j-th second. Then the i-th element will increase by (j+1) \* Ai and the element will become Ai + (j+1) \* Ai at (j+1)-th second.

Your task is to find the minimum cost to remove all the elements from the array A. As the answer can be very large, print the answer module 10⁹ + 7.

## Input format

- The first line of input contains a single integer T denoting the number of test cases.
- The first line of each test case contains a single integer N denoting the number of elements in the array A.
- The second line of each test case contains N space-separated integers, i-th integer denotes Ai.

## Output format

Print the answer corresponding to each test case in new line.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/harry-and-horcrux-1-df65f8e9/
