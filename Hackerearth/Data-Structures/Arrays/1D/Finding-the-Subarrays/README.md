# Finding the Subarrays

You are given an array A of N elements. You need to find all the subarrays such that their average sum is greater than the average sum of the remaining array elements. You need to print the start and end index of each subarray in sorted order in a new line.

- A subarray which starts at L1 position and ends at position R1 comes before a subarray that starts at L2 and ends at R2 if L1 < L2 or if L1 = L2 but R1 <= R2.
- The array indexes are in the range 1 to N.
- The average sum of an empty array is 0.

## Input format

- The first line contains an integer N that denotes the total number of elements in the array.
- The next line contains N space separated integers that denote the elements of the array A.

## Output format

The first line of output should contain an integer X that denotes how many subarrays that follow the given criterion are there.
The next X lines contain a pair of space-separated integers corresponding to the start and end positions of the valid subarrays.
