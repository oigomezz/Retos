# [Historic Heist][link]

Danny Ocean wants to score the biggest heist in history. His target? The MGM Grand. It's not an easy heist so he wants your help.

The city is in the form of a graph, there are N junctions connected by M bi-directional roads. The time taken to travel on the i-th road is ti. The MGM Grand is located at the junction with index s, whereas Danny's safe house is at junction d. There are several police stations in the city. In the case of any criminal activity, police units are dispatched from all the police stations immediately.

Now Danny wants to know the least amount of time in which he can reach the safehouse after completing the heist from MGM Grand without being intercepted by the police at any junction of the city.

**Note:** Police can only intercept Danny at any of the junctions in the city.

## Input format

- The first line consists of a single integer T denoting the number of test cases.
- The first line of each test case consists of an integers N, denoting the number of junctions.
- The second line of each test case contains N space-separated integers. If the i-th integer is 1, then it means that the i-th has the police station. It is 0 otherwise.
- Next line contains two integers s and d, denoting the junction with the MGM Grand and the safehouse respectively.
- Next line of each test case consists of an integer M and 3, denoting the number of roads in Byteland and the number of columns in the input.
- The following M lines contain three space-separated integers u, v, and t, where u and v are the numbers of the cities connected by this road and t is the time taken to travel on that road.

**Note:** Input contains self-loops and multiple roads between two junctions.

## Output format

For each test case, output a single integer denoting the least amount of time in which Danny can reach his safehouse avoiding the police. If no such path exists, then print -1 instead.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/money-transfer-c6c93a50/
