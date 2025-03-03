# Rewards and happiness

There are n people are living in a town. Each person has a set of friends. The properties of friendship in your town are as follows:

- It is symmetric: If A is a friend of B, then B is also a friend of A.
- It is not transitive: If A and B are friends and B and C are friends, then it does not implies that A and C are also friends.

The festival of the town runs for Q days. For each of the Q days, one person among those n people gets a reward in the morning. Initially, all the n people do not get any rewards.

A person in the town becomes happy if the total reward of his friends reach k. Your task is to determine the day when each person becomes happy.

## Input format

- First line:Two integers n,k denoting the number of people and the total rewards that makes the friend happy.
- Next m lines: A,B
- Next line: Q denoting the days that the festival runs.
- Q lines: p,x denoting that person p getting a reward x.

## Output format

Print n lines for each person that represents the day when the person becomes happy. If the person never becomes happy, then print -1.
