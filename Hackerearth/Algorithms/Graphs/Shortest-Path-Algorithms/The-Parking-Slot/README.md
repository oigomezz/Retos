# [The Parking Slot][link]

There is a parking facility which is in the form of a graph having N nodes and M edges. The graph does not have self loops or multiple edges.

Each node represents a parking slot and has a capacity of vehicles it can hold. Each edge (u,v) has a weight w representing we can reach from node u to node v incurring a cost of w units. All parking slots have a parking fee F per vehicle which is same for all slots. There are K identical vehicles entering the parking facility, each vehicle enumerated with a distinct number from 1 to K. The vehicles enter in their natural order, that is, vehicle number 1 enters, then vehicle number 2, then 3 and so on till vehicle number K.

For each vehicle, you have to print the minimum total cost that is incurred on the vehicle owner. Here, total cost includes cost of the path taken to reach the parking slot and parking fee of the slot.

It is guaranteed that you can reach any slot from any other slot.

All vehicles entering the parking facility enter from the parking slot 1.

## Input format

- The first line consists of three integers N, M and F, denoting number of nodes, number of edges and parking fee respectively.
- The second line consists of N space separated integers denoting the parking capacity of each parking slot. This array is represented by C[].
- Following M lines contain three space separated integers each: u,v and w, denoting we can reach from node u to node v incurring a cost of w units.
- The last line of input contains an integer K.

## Output format

Print K space separated integers denoting answer for each vehicle.i-th integer in the space separated integers denotes answer for i-th vehicle number. If it is not possible to park a vehicle , print -1 for that vehicle.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/the-parking-slot-9fac40d6/
