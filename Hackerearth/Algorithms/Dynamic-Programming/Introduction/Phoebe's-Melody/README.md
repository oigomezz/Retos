# [Phoebe's Melody][link]

Phoebe enjoys playing music. She especially enjoys playing it for her friends.

Phoebe has made a new musical instrument. The instrument is very much like a piano. It has N keys arranged in a straight line, numbered from 1 to N. The i-th key has volume Vi. No two keys have the same volume and 1 ≤ Vi ≤ N. It takes |i-j| time to move from the i-th key to the j-th key on the instrument. Phoebe has a unique way of playing music. Immediately after playing key i, she can play only a key j such that:

- j is not closer than K positions from key i (i.e. j should not be in the range [ i-K+1, i+K-1 ]).
- Vj < Vi.

Each key may have 0 or more keys that can be played immediately after it.

Phoebe wants to find the summation of time required to go from each key i to the closest key that can be played after it. If there is no next playable key for a key i, then consider its time taken as 0.

## Input format

- The first line of the input contains T, the number of test cases.
- The first line of each test case contains N and K. The second line of each test case contains N integers of the array V.

## Output format

For each test case, output a single number denoting the summation of time taken to move from each key i to the closest next playable key after i.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/phoebes-melody-1/
