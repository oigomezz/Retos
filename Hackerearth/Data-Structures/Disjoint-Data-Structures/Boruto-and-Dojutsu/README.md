# [Boruto and Dojutsu][link]

Boruto subconsciously awakened a Dojutsu (magic) in his right eye which has a lot of special powers. One of its powers includes the ability to track a target through its chakra (energy). One day while training, Boruto marks N targets, each of which has some color . Some of the targets are connected to each other, as a result of which these N targets form a colorful undirected graph G with N nodes (denoting the N targets), indexed from 1 to N and M edges (denoting the M connections between the targets), indexed from 1 to M.

Using the power of his eye, Boruto was able to find the number of distinct colors in the connected component containing any particular target. Now Boruto wants to know the number of distinct colors in the connected component containing any particular target if the connections between the targets are being removed dynamically. As he is at an early stage of learning how to use Dojutsu, he wants your help in getting the answer to this problem.

## Input format

- The first line of input contains 3 space separated integers N, M and Q denoting the number of targets, the number of connections between the targets and the number of operations to be performed respectively.
- The second line contains N space-separated integers, i-th of which denotes the color of the target i.
- The next M lines contain 2 space separated integers U and V which depicts a connection between targets U and V. i-th line denotes the i-th edge.
- This is followed by Q lines, each describing an operation in the following format:
  1. 1 X : Remove the connection (edge) numbered X.
  2. 2 Y: Print the number of distinct colors in the connected component containing target (node) Y.

## Output format

The output should consist of the answer to each of the operation of the 2-nd type printed on a new line.

[link]: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/strengthen-their-bonding-6eeb0e01/
