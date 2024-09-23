# Three arrays

You are given three arrays a[1...n], b[1...n], c[1...n] and two numbers M and K. Find a lexicographically minimum {x,y,z} such that there are exactly K indices i (1 <= i <= n) where x\*ai + y\*bi - ci\*z = M\*f for some integer f. Also, you are given ranges of x,y, and z -- l[1..3], r[1..3] (l1<= x <= r1, l2<= y <= r2, l3<= z <= r3). Here, a triplet of integers {x1,y1,z1} is considered to be lexicographically smaller than a triplet {x2,y2,z2} if sequence [x1,y1,z1] is lexicographically smaller than sequence [x2,y2,z2]. A sequence a is lexicographically smaller than a sequence b if in the first position where a and b differ, the sequence a has a smaller element than the corresponding element in b.

## Input format

- The first line contains one three integers n, m, k.
- The next n lines contain three integers ai, bi, ci.
- The next three lines contain two integers li, ri.

## Output format

If an answer does not exist, print -1. Otherwise, print desirable {x,y,z}.
