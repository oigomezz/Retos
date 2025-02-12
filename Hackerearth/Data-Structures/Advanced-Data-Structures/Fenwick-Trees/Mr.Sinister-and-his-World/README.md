# [Mr. Sinister and his World][link]

It is a very bad time for human race, as powerful mutant Mr. Sinister has taken control of the world. He is killing a lot of people. The world is one dimensional and at most one man can stay at one point of the world. The points are numbered from (1,0) to (INF,0) where INF denotes infinity.

As Sinister is killing humans, he wants to know the maximum distance between any two adjacent humans in the world. But a human can come or leave the world (goes to another planet) at a time. So, there will be three types of queries of the following form.

- 1 X - A human comes and occupies co-ordinate (X,0). It is guaranteed that before this query, there will be no human at the given point.

- 2 - You have to find out the maximum distance between any two adjacent humans and the position of these two humans. If there is a tie in the maximum adjacent distances, then print the one which has maximum X co-ordinate.

- 3 X - A human who currently occupies co-ordinate leaves the world. It is guaranteed that there will be a human at co-ordinate before this query.

Also, It is guaranteed that at any particular time there will at least two humans in the world.

As Mr. Sinister is not a very good programmer, can you help answer all queries of type 2 for him?

## Input format

- First line of the input contains a single integer T denoting the number of test cases in the input.
- Each test case starts with an integer N denoting the number of people initially in the world.
- The next line consists of N distinct space separated integers C[i], denoting the X co-ordinates of the initially present people.
- The next line contains a single integer Q denoting the number of queries.
- For each query, first integer will be type denotes the type of that query.
  - If type is 1 or 3, then there will be another integer X denoting the X co-ordinate where a human will come or leave depending upon the type of query.

## Output format

For each query of type 2, print three integers, the maximum distance between any two adjacent humans and the co-ordinate of this two humans. The co-ordinate have to be printed in increasing order.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/mr-sinister-and-his-world-4cc82c88/
