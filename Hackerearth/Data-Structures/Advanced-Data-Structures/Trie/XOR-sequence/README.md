# [Xor sequence][link]

Given a sequence a1 ... an. You need to perform m queries on it.

In each query, two parameters x,y are given, and we let

- l = min(((x + ans \* t) mod n) + 1, ((y + ans \* t) mod n) + 1)
- r = max(((x + ans \* t) mod n) + 1, ((y + ans \* t) mod n) + 1)

In this statement, t is a given constant, which can be 0 or 1. And ans is the answer of last query, with initial value is 0.

You need to find a pair (i,j), satisfies l <= i <= j <= r, and maximize ai xor ai+1 xor ... xor aj.

The answer of this query is ai xor ai+1 xor ... xor aj.

## Input format

- The first line contains three integers, n, m, and t.
- The second line contains n integers, representing the sequence a.
- The next m lines, each line contains two integers, x and y.

## Output format

For each query, output an integer represents the answer.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/xor-sequence-aad3111f/
