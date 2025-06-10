# [Buying items][link]

There are n different types of objects. You want to buy atleast one instance of each type of object. There are m people , each of them sells one set of objects at a certain price (price is for the set).

Each of these m people sells either nothing or all the objects in the set he has. Information of these m sellers is represented by matrix M of size m\*n. if Mij = 1, it means that i-th seller has one j-th type of object in his set, otherwise Mij = 0. The i-th seller will sell set of all his objects at price Ci.

You want to buy at least one object of each type (it is guaranteed that it is always possible to do so). Find the minimal cost needed to pay to achieve it.

## Input format

- The first line contains two integers n,m separated by space.
- The (i+1)th line contains (n+1) integers - Mi1, Mi2, Mi3, ..., Min, Ci.

## Output format

Output the minimal cost you should pay to buy at least one object of each type.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/buying-items-d552af6f/
