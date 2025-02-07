# [Update And Query][link]

Deepankar loves to play with the arrays a lot. Today, he has an array A of N integers. He has to fulfill M operations. Each operation has one of the following two types:

- U X Y : Update the value at the X-th index of the array with Y.
- Q X C : Calculate the length of the longest subarray that starts at Xth index and satisfy following inequality, A[X]-C ≤ V ≤ A[X] + C, Where V is any value from the chosen subarray.

Deepankar is facing difficulty in maintaining the efficiency of the operations. Can you help him in accomplishing this task efficiently.

## Input format

- First line of input contains two integers N and M denoting the number of elements in the array and number of operations to be performed over this array.
- Next line of input contains N space separated integers denoting the elements of the array.
- Next M lines of input contains M operations (1 operation per line). Each operation is in one of the two form described above.

## Output format

For each operation of type Q, You need to print two values to the output.

- V1 : Length of the longest subarray that starts at Xth index and satisfy mentioned inequality.
- V2 : Minimum value Z such that following inequality holds A[X] - Z ≤ V ≤ A[X] + Z Where V is any value from the chosen subarray .

If in case there does not exist any such subarray then print -1 -1 to the output.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/update-and-query/
