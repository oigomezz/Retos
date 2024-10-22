# Boring Not boring problem

You are given two integers n (1<=n<=10⁵) and m (1<=m<=10⁵). Initially, you have an array a of n zeros, and applied queries on it. Query is given as l r x, where you apply ai = ai xor x (xor denotes the operation bitwise XOR) for every between l and r. But this problem seems boring, so Almas modify some queries interval. By modifying, he applied that operation on a subset of positions on a segment(maybe empty subset). Now he asks you how many different arrays he could have after applying queries. Since the answer can be large, output by modulo 1000000007 (10⁹ + 7).

## Input format

- In first line, you are given two integers n and m.
- In next m lines, you are given l r x.

## Output format

Print in a single line answer by modulo 10⁹ + 7.
