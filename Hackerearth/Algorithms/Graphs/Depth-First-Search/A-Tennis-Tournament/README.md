# [A tennis tournament][link]

There was a tennis tournament held recently and Sylvie was following the matches when she noticed something odd. She knows for a fact that in this tournament someone will win against someone else if and only if they are better than them and there is no draw in the games.

She observed that some winning loops were formed in the tournament, meaning that if among players z1 to zk, for each i from 1 to k-1, zi had won against zi+1, then the player zk had won against z1 which should be impossible. Therefore, she suspected that there was some doping involved.

She wanted to report it to the tournament organizer so they can act accordingly but to prove her point she wanted to give them an example. She decided to provide them with the smallest loop possible so verifying it would not be so hard. Now, you have to help her find the smallest loop.

In other words, there is a directed graph and you have to find the smallest cycle possible.

**Note:** The graph does not have any self-loops but multiple edges are allowed.

## Input format

- The first line contains integers n and m denoting the number of players and the number of matches respectively.
- Each of the next m lines contains two integers x,y which means there was a match between x and y that x had won against y.

## Output format

- In the first line of output, you should print a single integer r represents the length of the smallest winning loop in the tournament.
- In the next r lines, print two integers x and y in each line which represents one of the matches in the winning loop that you have found and x had won against y in that match (an edge of the graph).

**Note:** If there is no winning loop in the tournament (cycle in the graph), then print -1 in the only line of output.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/approximate/tennis-tournament-75939265/
