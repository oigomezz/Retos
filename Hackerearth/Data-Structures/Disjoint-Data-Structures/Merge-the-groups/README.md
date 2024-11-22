# Merge the groups

You are given an array A of N elements. Each element belongs to its own group initially.

You need to process the following two types of queries:

- 1 X Y - The array elements which are at positions X and Y in the array A merge their group.
- 2 X - Print the maximum absolute difference of the array values that belong to the group of X-th element of the array.

Note: It is possible that the elements X and Y in the query of type 1 already be in the same group. You need to simply ignore that query.

## Input format

- The first line contains an integer N as input that denotes the total number of elements of the array.
- The next line contains N space separated integers that denote the elements of that array.
- The next line of input contains an integer Q that denotes the total number of queries.
- The next Q lines contain description of each query.
- The description of each query begins with an integer type which is 1 for 1st type of queries and 2 for second type of queries.

## Output format

For each query of type 1, print the answer in a new line
