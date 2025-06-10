# [Metro][link]

A city subway line has become huge and it is hard to take the shortest path through them. You have to find the shortest path in subway lines. In the second 0, you are in the station start and you want to go to the station end.

The city has n stations. The subway has m lines. Each subway line goes to some stations.

The i-th subway goes to stations ui1, ui2, ..., uik (in order) and this train takes wij seconds to travel from uij to uij+1 (for 1 <= i <= m and 1 <= j < k).

Trains are ready for the passengers to get in, but the last train goes in the second ti (and you are allowed to board it in between the path).

## Input format

- The first line contains n,m (in order).
- Next 3\*m lines describe subway lines.
- The first line contains ki, ti and next line contains ui1, ui2, ..., uik and the next line contains w1, w2, ..., wk.
- The last line containts start, end.
- It is guaranteed start != end and no subway line intersects itself.

## Output format

Print the shortest path in subway lines from the station start to end. If there is no way from start to end, print -1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/metro-6db2ba1b/
