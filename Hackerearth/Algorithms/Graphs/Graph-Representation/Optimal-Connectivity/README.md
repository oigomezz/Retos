# [Optimal Connectivity][link]

A company X has a network of N computers. There are N-1 links in the network, each link connecting a pair of computers. Each link has a particular time lag in between the two computers. It is assured that all the computers are connected.

The engineers at X assume that the current status of the network is a bit slow and they want to improve it. So they experiment with Q computer pairs.

For each of these Q pairs, you are given new direct link's time lag between the pair of computers. If these two computers are directly connected using the new link and some old link is removed from the network, you need to check if the network become better.

A new network is better than older if the sum of all the time lags is strictly lesser in the new network than the old one and the network is still connected.

**Note:** All queries are independent. That is, for each of the Q pairs, old network is the initial given network.

## Input format

- The first line contains an integer N denoting the total number of computers.
- Each of the next N-1 lines contains a triplet of integers (u,v,w) which states that the computer with the number u is connected to the computer with the number v and the time lag is of w units.
- The next line contains an integer Q.
- Each of the next Q lines contains three integers u,v and w which states that the new direct link between computer with the number u and computer with the number v has the time lag of w units.

## Output format

For each query, you need to print YES if you can improve the network by adding this link else print NO.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/optimal-connectivity-c6ae79ca/
