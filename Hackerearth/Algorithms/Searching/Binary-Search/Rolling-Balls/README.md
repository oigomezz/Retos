# [Rolling Balls][link]

There is a segment of length L-1 meters, and there are L positions on it, numbered 1,2,...,L, equally spaced by 1 meter apart each, in the given order. There are n balls on it, at positions s1,s2,...,sn (si < s(i+1)). Each ball is either rolling to the left of to the right at the speed of 1 meter/second. Whenever two balls hit each other, both of them change direction instantly but keep the same speed. A ball also changes direction when it reaches one of the ends of the segment (position 1 or L). You are given q queries, each one gives you two numbers ti and pi, and you should output the position of the pi-th ball after ti second.

## Input format

- The first line contain three integers: L, n and q.
- The second line contains n distinct integers s1,s2,...,sn (si < s(i+1))
- The third line contains n integers d1,d2,...,dn ( di = 0 if the i-th ball rolls to the left and di = 1 if it rolls to the right).
- The following q lines each contain two numbers: ti and pi.

## Output format

Print q lines, each containing a single integer: the i-th line should contain the answer to the i-th query. It can be proved that the answer is always an integer.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/rolling-balls-b8923a50/
