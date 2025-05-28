# [Optimal Edge Weights][link]

There is a state (territory) which is a tree rooted at node 1. All the cities (numbered from 1 to N+1) in this state are connected via bidirectional roads. You have to add toll tax on each road. There are N roads which connect the cities of the state. You have to assign toll taxes on the roads so as to maximize the function Toll described below:

```C
for(i=1;i<=number of cities;i++)
{
    for(j=i+1;j<=number of cities;j++)
    {
        toll+=(toll required to pay to travel from i to j)
     }
}
```

You have to maximize the toll tax. Assign the roads by toll taxes from the given array A (using each value exactly once). Find the maximum toll obtained.

## Input format

- First line contains N and an integer whose value is always 2.
- Then N roads follow containing 2 integers u and v, denoting the cities between which the road is.
- Next line contains N space separated values denoting elements of array A.

## Output format

Print the maximum toll which can be obtained.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/loan-for-travel-24cf67a1/
