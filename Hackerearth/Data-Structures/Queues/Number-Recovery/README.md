# [Number Recovery][link]

A positive integer X has been stolen. But luckily, N hints are available, each described by two integers ai and di, meaning that |X - ai| = di. The hints are numbered 1 through N. While some of those hints are helpful, some might be just a lie. Therefore, we are going to investigate the number X under different possible scenarios.

Initially, we neither trust nor distrust any hint. That is, each hint may be either true or false. Then, in each of the Q stages, we will either:

- 1 id: Entrust the id-th hint (1 <= id <= N). That is, from now on, the id-th hint must be true, unless declared otherwise in the future.

- 2 id: Distrust the id-th hint (1 <= id <= N). That is, from now on, the id-th hint must be false, unless declared otherwise in the future.

- 3 id: Neutralize the id-th hint (1 <= id <= N). That is, from now on, the id-th hint may be either true or false, unless declared otherwise in the future.

After each stage, you should determine the number of possible positive values X and report such values in an increasing order. If there are infinitely many such values, print -1 instead.

## Input format

- The first line contains two space-separated integers N and Q.
- The i-th of the following N lines contains two space-separated integers ai and di, describing the i-th hint. It is guaranteed that no two hints are identical. That is, for every two different i, j, it is guaranteed that ai != aj or di != dj.
- Then, Q lines follow, each containing two integers t and id — the type of an update and the index of an affected hint.

## Output format

After each stage, print the number of possible values of X (in case there are infinitely many of them, print -1). If the number of possible values is finite and non-zero, in the same line, continue to print those values in an increasing order.

[link]: https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/number-recovery-0b988eb2/
