# Previous Coprime Element

Given an Array arr of length N find the index (0-indexed) of previous co-prime element for each index 0 <= i < N, or -1 if there's no such value.

Two values x and y are called co-prime if GCD(x,y) = 1.

Previous co-prime element of arr[i] is the first element co-prime to arr[i] on the left of index i, ie. maximum j such that GCD(arr[i],arr[j]) = 1 and j < i, or -1 if there's no co-prime element to the left of arr[i].

## Input format

- First line contains an integer T denoting the number of test cases.
- First line of each testcase contains an integer N denoting length of arr.
- Next line contains N space-seperated integer, denoting the elements of arr.

## Output format

For each testcase, In a single line, print the index of previous co-prime element of arr[i] for each index 0 <= i < N, or -1 if no such value.
