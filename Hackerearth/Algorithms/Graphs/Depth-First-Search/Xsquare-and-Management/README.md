# [Xsquare And Management][link]

Xsquare has recently started an organisation named HackerEarth. Xsquare has hired N employees having employee ID numbered from 1 to N to work within the organisation. Organisational structure is divided into a number of departments. Each of the N employee is hired to work under exactly one department. All the employees working under the same department are somehow related to each other.

More specifically, organisational structure is represented in the form of a forest containing one or more connected components, where each connected component represents a department and contains the IDs of employees working in that department. A department can be represented in the form of a tree.

## Departments

- employees with ID number {1,3,5,8} work in the same department.
- employees with ID number {4,6,7,10} work in the same department.
- employees with ID number {2,9,11} work in the same department.

As it is just starting days of the organisation, Xsquare decided to maintain the minimum management level within the organisation. For the purpose to be served, Xsquare has decided to select exactly one employee from each department who will be the manager of that particular department. The Manager would thus form the root of the tree representing the department from which he got selected.

## Terminologies Involved

- **Department's Management Level**: Management level of a department is defined as the height of the tree representing that department and height would obviously depend upon the root of that department being chosen.
- **Organisation's Management Level**: Management level of the organisation is defined as maximum of all department's management level.

Xsquare is busy managing resources for his organisation. Therefore, he cannot participate in the electing the manager for each department.

Can you help him in accomplishing this task ?

Your task is very simple. You have to count the number of ways of selecting manager from each department such that the management level of his organisation is minimum. Since the answer can be large, output it modulo ( 109 + 7 ).

## Input format

- First line of input contains a single integer T denoting the number of test cases.
- First line of each test case contains two space separated N and M denoting the number of employees and number of edges in the tree.
- Next M lines of each test case contains two space separated integers U and V denoting the employees that are related to each other in some or the other way.

## Output format

For each test case, print out the required answer in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/xsquare-and-management/
