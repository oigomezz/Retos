# [Elevator Overload][link]

A corporate building has n floors numbered from 1 to n. An elevator starts moving from the floor 1 and goes upward until it reaches floor the n. It has the maximum capacity of weight (W) and persons (P) it can lift. It will stop at every floor and there will be some number of employees who will get into the elevator and also some of the employees will leave it as they have reached their desired floors. At every floor, those who have reached the desired floor will leave first and then those who were waiting for the elevator will get in. As the elevator has a maximum limit of weight and persons (when any one of the limits is exceeded, the overload sign is displayed), it will permanently stop where the overload situation happens or it will permanently stop at floor n if no overload situation happens. You need to find the floor, where the elevator will stop permanently.

Note: If an employee gets in at floor x, then it is guaranteed that his desired floor will be greater than x and less than or equal to n. There are no employees waiting at floor n.

You have to answer for t number of test cases.

## Input format

- The first line will contain one integer t, which denotes the number of test cases.
- For every test case:
  - The first line will have a single integer denoting the number of floors in the building i.e. n.
  - Second line will have two space separated integers representing the values of P and W.
  - Third line will have a 1-indexed space separated array of n-1 integers where ith integer will represent the number of employees waiting for the elevator at floor i.
  - In next 2 \*(n-1) lines, for every floor, there will be 2 lines of space separated integers where the first line represent the desired floor and second line will represent the corresponding weight of the employees waiting at that floor.

## Output format

Output will have single integer denoting the floor number where the elevator will permanently stop.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/lift-trouble-7e3bc27d/
