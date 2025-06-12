# [Mancunian Goes To The Derby][link]

It's derby weekend in Manchester. United vs City. The Red Devils vs The Noisy Neighbours. Mancunian has been waiting for this for a long time. But due to the huge popularity of the match, there is a lot of traffic on the streets. To control the rush, the police have devised an ingenious system of one-way roads which ensures smooth flow of traffic.

The city of Manchester can be modeled as a graph of N nodes and E edges. Vertices are numbered from 1 to N. Each edge is a one-way road but direction depends on the time at which roads are traversed. If there is a road between checkpoints A and B, it is directed from A to B in even-numbered seconds and B to A in odd-numbered seconds. Mancunian can move between adjacent vertices taking time 1 second. He can always choose to wait at some checkpoint for the roads to change their orientation. Mancunian's house is located at the point numbered 1 and the venue of the match, Old Trafford (the Theatre of Dreams) is located at point N.

Given Q possible start times, for each query you have to find out whether Mancunian can reach the stadium before the start of the match. He always starts his journey at time 0.

## Input format

- The first line contains three integers N, E and Q denoting the number of checkpoints, number of roads in the city of Manchester and the number of possible start times of the match respectively.
- Each of the next E lines consists of two integers A and B describing a road in the city. It is guaranteed that there is no self-loop or multiple edge in the road network. Note that the line A B in the input is different from the line B A as they are directed opposite to each other.
- The i-th of the next Q lines contains a single integer, the i-th possible start time Ti of the match,

## Output format

Print Q lines. Each line should contain a single word. Print "GGMU" (without quotes) if Mancunian can reach the stadium on time, and "FML"(without quotes) otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/mancunian-goes-to-the-derby/
