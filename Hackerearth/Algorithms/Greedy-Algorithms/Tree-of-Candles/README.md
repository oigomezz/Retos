# [Tree of Candles][link]

This Diwali, El has decided to create a tree-like candle structure. El has N candles numbered from 1 to N arranged in the form of a tree, rooted at candle-1. The i-th candle can burn for Ci minutes and then it vanishes completely.

El now wants to light the candles, but he has some constraints. He can light only one candle a minute and to light a candle, all of its ancestors must have been lit. He wants to know if there exists an order to lit the candles following the above constraints such that all candles are burning simultaneously, if there exists such order, what is the maximum number of minutes all candles can burn simultaneously.

Print only one integer: The maximum number of minutes all candles can burn simultaneously, if it not possible for all candles to burn simultaneously then print 0.

## Input format

- The first line contains t, the number of test cases.
- For each test case first line contains N, The number of candles in the tree.
- Second line of each test contains N space separated integers C1 to Cn, Burning time of each candle.
- Following N-1 line contains 2 space seperated integers x,y denoting that there exists an edge between x and y.

## Output format

For each test case print a single integer: The maximum number of minutes all candles can burn simultaneously, if it not possible for all candles to burn simultaneously print 0.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/tree-of-candles-912e495c/
