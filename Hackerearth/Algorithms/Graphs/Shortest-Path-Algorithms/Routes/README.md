# [Routes][link]

A consultant earns an amount K per hour of his time. He has to fly from city A to city B spending the least cost. Every hour that he spends traveling or waiting in an airport for connecting flights, he is losing an amount K. Assume that layover time between connecting flights is always one hour. Given inputs as N - the number of cities, X – the number of routes between cities (not all cities are necessarily connected), costs and time of flights between two cities for X routes (same in both directions), the source city number S and the destination city number D , please output the most optimal route S -> [ any intermediate cities ] -> D, total time in hours T and total cost C (including opportunity cost of lost earnings).

## Input format

- The first line contains K.
- The second line contains N.
- The third line contains X.
- Next X lines contain X route quadruplets involving source city number, destination city number, flight time and flight cost
- Next line contains S.
- Next line contains D.

## Output format

Print the optimal route in the follow format: S->[C1 -> C2 -> … -> Cy]-> D T C. If there is no route possible or if any of the constraints is failing, print Error.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/routes-48c6192a/
