# [Mancunian And Liverbird Go Bar Hopping][link]

It's April Fools' Day 2017 and to celebrate, Mancunian and his arch-enemy Liverbird decide to put aside their differences and go have a drink together.

There are N bars (numbered from 1 to N) located in a straight line. The i-th is located at point i on the line. Apart from this, there are N-1 roads, the i-th of which connects the i-th and i+1th bars. Note that the roads are unidirectional. You are given the initial orientation of each road.

On celebratory occasions such as these, there are a lot of people on the streets. Hence, the police have to take special measures to combat traffic congestion. Periodically, they issue a directive to reverse the direction of all the roads. What this means is that, if there was a road directed from bar numbered i to bar i+1, after the update, it will be directed from i+1 to i.

You are given a set of operations. Each operation can be either an update or a query. Update is the one described above. In each query, you are given the location of the bar the two partyers are located at currently. You have to count the number of bars (including the current location) that are reachable from their current location.

## Input format

- The first line contains a single integer N denoting the number of bars on the road.
- The second line contains N-1 integers denoting the directions of the roads. The i-th integer is 1 if the i-th road is directed from i to i+1 and 0 if directed from i+1 to i.
- The third line contains a single integer Q denoting the number of operations.
- Each of the next Q lines is either an update or a query.
- An update is given by a single character U.
- A query is given in the form of the character Q followed by an integer S denoting the current location of the pair.

## Output format

For each query, output a single integer which is the answer to the corresponding query.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/mancunian-and-liverbird-go-bar-hopping-2/
