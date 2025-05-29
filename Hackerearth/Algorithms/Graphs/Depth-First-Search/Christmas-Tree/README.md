# [Christmas tree][link]

Little Santa have to give gifts to N children. There are N-1 roads connecting the homes of N children. Each road has some special Santa tax value which only Santa have to pay. Little Santa is wondering what is the realK-th minimum tax value in the path between the home of child realA and child realB.

**Note:** k-th minimum value in a list A is k-th value in the list A after sorting A.

## Input format

- First line contains one integer, N, denoting the number of children.
- Next N-1 lines contains three space separated integers each, x,y,w, denoting that home of child x is connected to home of child y and the tax value of the road is w.
- Next line will contain an integer, q , denoting the number of queries.
- Next q lines contains three space separated integers each, a,b and k.

- To generate realA and realB you have to use following formulas:

  - realAi = ((ai - 1 + max(0,lastAns)) mod n) + 1
  - realBi = ((bi - 1 + 2\*max(0,lastAns)) mod n) + 1
  - realKi = ((Ki - 1 + 3\*max(0,lastAns)) mod n) + 1

Where lastAns is answer for previous query, or 0 if this is the first query.

## Output format

For each query, print the number the realK-th minimum tax value in the path between the home of child realA and child realB. Print 1 if there is no such value.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/christmas-tree/
