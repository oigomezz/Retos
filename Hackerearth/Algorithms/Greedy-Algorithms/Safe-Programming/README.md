# [Safe programming][link]

You are developing the habit of "Safe Programming." You are given N unsigned integer data types of sizes (in bits) a1, a2, a3, ... , an. If the i-th datatype has size ai bits, you can store all integers from 0 to 2^(ai) - 1.

The rule of safe programming is as follows:

- If n is a number that can be represented by the bit size ai, and if at least one aj > ai is present in the given array, then we must be able to represent n3 by any one of the bit sizes given in array a.

## Input format

- The first line contains N denoting the number of available variations of bit sizes
- The second line contains N space-separated integers denoting the available bit sizes.

## Output format

Output 1 if it is safe programming; else, output 0.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/safe-programming-d5cf9331/
