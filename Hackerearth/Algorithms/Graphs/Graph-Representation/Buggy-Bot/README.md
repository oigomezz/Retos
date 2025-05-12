# [Buggy Bot][link]

Alice finally finished her CS assignment and programmed her robot to explore a directed graph G with n nodes (numbered 1 through n) and m edges.

Alice programmed the robot with a series of k instructions. The robot will attempt to execute one instruction per second in the given order; it won't repeat any instruction or return to an instruction it didn't execute. Each instruction is of the form "if the robot is currently at node x, it will move to node y". Note that if the robot is not currently at node x, it will ignore such an instruction. The robot is initially located at node 1.

Unfortunately, the robot is a bit buggy — at one moment in time, it can move from its current node to an arbitrary neighboring node (a node to which an edge leads from the current node). Note that this bug could have happened before any instructions, between any two instructions, or after all instructions; however, it couldn't have happened multiple times. It is also possible that this bug did not happen at all.

Alice is having trouble debugging the robot, and would like your help to determine all nodes where the robot could be located at the end.

## Input format

- The first line of the input contains three integers n, m and k, denoting the number of nodes, the number of edges and the number of instructions respectively.

- Each of the following m lines contains two space-separated integers ai and bi denoting a directed edge from node ai to node bi.

- Each of the following k lines contains two space-separated integers xi and yi denoting an instruction for the robot.

## Output format

- On the first line, print a single integer F — the number of possible final nodes for the robot.
- On the second line, print F space-separated integers, representing the possible final nodes for the robot, in increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/buggy-bot-d8f6eb53/
