# [Meet people][link]

You are given a tree of N nodes and K people located on the tree. You are also given an array A of size K where Ai indicate the location of the i-th person.

Now, there is an emergency meeting so all K people want to meet as soon as possible at the same node. In one second, a person who is standing at the i-th node can go to any adjacent node of the i-th node (the person cannot stand at the i-th node and he or she has to move).

You are required to print the minimum time to meet all K people at the same node. If it is impossible to meet all K people at one node, then print -1.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case contains integers N and K denoting the total node of tree and total number of people.
- Next N-1 lines of each test case contain two integers x and y. It means that there exists an edge connecting vertices x and y. It is guaranteed that using these edges always forms a tree.
- The next line of each test case contains K distinct integers A1,A2,...,Ak where Ai is the location of the i-th person.

## Output format

For each test case, print the minimum time to meet all K people at the same node. If it is impossible to meet all K people at one node, then print -1 in new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/emergency-meeting-da1fc0b5/
