# [StellarSeating Maximization][link]

In the realm of StarRail, a grand interstellar train known for its luxurious compartments, each carriage comes with a unique seating arrangement denoted by an array S. The array S represents the number of seats in each compartment, adding to the train's charm and comfort.

A brilliant engineer named Nova has been entrusted with the task of enhancing the seating capacity of the StarRail.

Nova possesses a unique ability: he can perform the following operation atmost once. This operation enables Nova to select two compartments, denoted by indices L and R, and modify the number of seats in all compartments between L and R (inclusive) by performing a bitwise XOR operation with value Y, where 1 <= L <= R <= N.

Mathematically, the operation can be expressed as follows: S[i] = S[i] ⊕ Y (⊕ denotes the bitwise the XOR operation), where L <= i <= R.

Nova's ultimate objective is to maximize the overall seating capacity of StarRail using this operation.

Help Nova determine the maximum number of passengers that can travel on the StarRail by finding the optimal compartments to perform the operation on and maximizing the total seating capacity.

## Input format

- The first line of input data contains single integer T, the number of test cases in the test.
- For each testcase the first line contains two integers N, the number of compartment in StarRail and Y, the number given to Nova.
- The second line contains N integers S1,S2,...,SN the number of seats in each compartment.

**Note:** Sum of all N doesn’t exceed 10⁶

## Output format

For each testcase output a single integer - the maximum number of passengers that can travel on the StarRail.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/stellarseating-maximation-challenge-3956f496/
