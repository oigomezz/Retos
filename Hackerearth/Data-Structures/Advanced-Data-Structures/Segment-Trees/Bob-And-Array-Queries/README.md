# Bob And Array Queries

Bob has an array A[] of N integers. Initially, all the elements of the array are zero. Bob asks you to perform Q operations on this array.

There are three types of operations that can be performed:

- 1 X: Update the value of A[X] to 2 \* A[X] + 1.
- 2 X: Update the value A[X] to [A[x]/2], where [] is Greatest Integer Function.
- 3 X Y: Take all the A[i] such that X <= i <= Y and convert them into their corresponding binary strings. Now concatenate all the binary strings and find the total no. of '1' in the resulting string.

**Note:** It is guaranteed that there is at least 1 type-3 query in the every test case. All the array elements will fit into 64 bit integers.

## Input format

- First line consists of two space-separated integers N and Q.
- Next, Q lines consist of Q operations of either of the 3 types as described above.

## Output format

For each type-3 query print the answer that is the no. of '1' in the resulting string.
