# Costliest Data Plan

Pawan has a finite number of friends, each friend has a unique non-negative number associated with him. (0, 1, 2..)

Pawan plans to host a party and has to send notifications to his friends.

A friend attends the party if he receives at least 1 notification from Pawan.

To send notifications, Pawan buys data plans Pawan can send notifications using data plan X in the following way:

- Let's say Data plan X costs Y.
- Then a friend associated with the number will receive a notification if and only if the ith bit in Y is set.

Now Pawan wonders if he can cut costs. Let him know the maximum cost that he can cut by removing at most 1 data plan and still being able to invite all the friends he could invite earlier

## Input format

Each test contains multiple test cases. The first line contains a single integer t (1≤t≤100) — the number of test cases. Description of the test cases follows.

The first line of each test case contains one integer N - the number of data plans.

The second line of each test case contains N integers a1,a2,…,an — the cost of data plans array.

It is guaranteed that the sum of N over all test cases does not exceed 10⁵

## Output format

For each test case, print a line containing a single integer – the maximum possible money that Pawan can save (print 0 if no data plan can be removed)
