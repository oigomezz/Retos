# Alice's construction

Alice has a warehouse with n boxes and the ith box has number pi. All box numbers are different and range from 1 to n. Alice wants to rearrange the boxes in the following way:

- First, she chooses some interval of boxes, starting from the Lth to the Rth inclusive, as well as some number X.
- Then arbitrarily chooses a pair of indices i and j from the interval [L;R] such that |i-j| = 1 and pi <= X, pj <= X and changes the boxes at positions i and j. That is, an arbitrary number of times swaps a pair of adjacent boxes in which the numbers do not exceed X.

You are given m triplets Li,Ri,Xi. For each of them, Alice asks you to tell how many different sequences of boxes she can get by selecting the following values.
Since these numbers can be very large, you need to subtract the remainder of their division by the prime number 10⁹ + 7.

**Note:** Two sequences of boxes are considered different if there is a position in which the boxes in both sequences have a different number.

## Input format

- The first line contains two integers n and m denoting the number of boxes in the warehouse and the number of triplets for which you need to find the number of ways.
- The second line contains n integers pi denoting the box numbers in the order in which they are located in the warehouse.
- The next m lines contain triples of integers Li, Ri, Xi.

## Output format

Print m lines where the ith line contains the remainder of dividing the number of possible sequences for the ith triple by 10⁹ + 7.
