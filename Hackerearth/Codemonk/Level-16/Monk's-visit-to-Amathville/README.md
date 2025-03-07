# Monk's visit to Amathville

Monk visits the small town of Amathville. Amathville is a town of integers where numbers reside peacefully with each other. There are N citizens in Amathville i.e. integers 1 to N. Two integers are friends, only if they are mutually co-prime.
The Mayor of Amathville has a problem for Monk to solve. He wants Monk to build an army out of the citizens of Amathville, such that all the citizens in the army are friends i.e. each citizen in the army has to be friends with every other and the army has to be as large as possible. If there are multiple possible combinations of army of same size, choose the one that is lexicographically smallest, when sorted in ascending order. Check the sample case for further clarity.

Post this, Monk also has to arrange the army in the formation of a single line. Adjacent friends can have frictions between them, i.e If an integer I is placed after an integer J in the line, this amounts to a friction of (I \* J) mod P units.

Help Monk solve the problem for the Mayor, by choosing the army and then minimizing the total friction of army. Report the minimum total value of friction.

## Input format

The first line consists of integer T. T testcases follow.
The first line of each testcase consists of two space-separated integers N, P.

## Output format

For each testcase, print the answer in a single line.
