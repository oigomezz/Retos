# Lottery

There is a lottery winner who has lives in a house which has R \* C rooms such that there are R rows where each row has C rooms and C columns and each column has R rooms, he will receive N coins worth Xi $ as a winner. He will place each coin in one of R \* C rooms and also note that more than one coin can be placed in a single room. You will be given which rooms he has chosen. Now robbers have known about the coins and want to loot him as much as possible. Robbers will do the following:

1. Column wise: For every column they will choose at most one coin to rob.
2. Row wise: For every row they will choose one coin to rob.

If they rob coin i, they will get an amount worth Xi and it is obivious that robbed coins will not be persent. They will rob optimally.

What is the maximum possible sum of amount robbers can rob?

## Input format

- The first line contains the number of test cases denoted by T.
- The first line of each test case contains three space seperated integers N, R, and C.
- Next N lines of each test case contain three integers X, Y, and Z denoting coin of worth Z $ is kept at the Y-th column of the X-th row.

## Output format

For each test case: Print a single line denoting the maximum amount that can be robbed.
