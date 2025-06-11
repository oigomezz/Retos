# [Chocolate Journey][link]

You live in the city B. Your friend is living in the city A. You need a special chocolate xyz. The chocolate is not available in your city and is available only at k cities. There are N cities in the country and M bi-directional roads between the cities and length of each of these bi-directional roads is given. The chocolate is preserved in cold containers and can stay for infinite time if it is preserved in those containers. If it is once taken out of the cold container, It expires in x units of time and you cannot put it back into the cold container to make it available for the infinite time.

It takes 1 unit of time to cover 1 unit of distance.

What is the minimum amount of time your friend needs to reach you with the chocolate?
If it is not possible to reach you with the chocolate, print "-1" ( without quotes ).

**Note:** There are no self loops and no multiple edges.

## Input format

- The first line contains four integers N (number of cities), M (number of bidirectional roads), k (number of cities where chocolate is available), x (the expiry time).
- The next line contains k space separated integers denoting cities where chocolate is available(Assume cities are indexed from 1 to N).
- The next M lines contains 3 integers u, v, d in each line indicating that there is a path between u and v and having a length of d.
- The last line contains 2 space separated integers A and B denoting your friend's and your city respectively.

## Output format

Print the minimum amount of time taken to reach the city B from A with the chocolate. If it is not possible, print "-1" (without quotes).

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/successful-marathon-0691ec04/
