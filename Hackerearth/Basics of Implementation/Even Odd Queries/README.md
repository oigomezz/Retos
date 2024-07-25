# Even Odd Queries

You are given an array Arr of size N, containing integers. You have to answer Q queries where each query is of the form:

- K L R :- If K = 0, then you have to find the probability of choosing an even number from the segment [L,R] (both Inclusive) in the array Arr.

- K L R :- If K = 1 , then you have to find the probability of choosing an odd number from the segment [L,R] (both Inclusive) in the array Arr.

For each query print two integers p and q which represent the probability p / q. Both p and q are reduced to the minimal form.

If p is 0 or p is equal to q print p / q alone.

## Input format

- First line: T i.e Number of testcases.
- For each testcase:
  - First line: Two space separated integers N and Q.
  - Second line: N space separated integers denoting the array .
  - Next Q lines: Three space separated integers K L and R.

## Output format

Output the answer to each query in a separate line.
