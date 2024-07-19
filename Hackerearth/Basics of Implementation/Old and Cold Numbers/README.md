# Old and Cold Numbers

Let's define Old number as a number X, such that it is divisible by count of odd integers in the range 1 to X. If number does not hold this property, then such number is defined as Cold number.

You are given an array A and Q tasks of the form L R, you have to find what is the minimum numbers of steps needed to make subarray from L to R balanced.

Any subarray is said to be balanced if count of Old number(s) is not less than count of Cold number(s) in that subarray. In every step, you can either increase the value of some array element by 1 or you can decrease an array element by 1.

**Note:** All tasks are independent of each other.

## Input format

- First line contains an integer T, denoting the number of testcases.
- In each test case:
  - First line contains N, the number of elements in array A.
  - Next line contains N space separated integers denoting array elements.
  - Next line contains Q, the number of queries.
  - Each of the next Q lines contains two space separated integers L and R.

## Output format

For each task, print total number of steps needed to change the subarray such that subarray from L to R is balanced.

Answer for each task should be printed in a new line.
