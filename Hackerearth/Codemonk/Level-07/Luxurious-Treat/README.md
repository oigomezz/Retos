# Luxurious treat

A city has N hotels located in the form of a tree and they are connected by roads.

**Note:** A connected undirected graph consists of N vertices connected by N-1 edges.

Each hotel has a fixed amount of money that they charge irrespective of the amount of food that is consumed. You are given the amount A[i]. You want to treat your friends in four different hotels with no limitation on the total amount that you can spend. You and your friends start your journey from the hotel located at the root and travel to the hotel located at any of the leaves through a simple path. You select four different hotels at random P, Q, R, and S that are located on this simple path.

_Note:_ Here, P is the ancestor of Q, Q is the ancestor of R, R and is the ancestor of S.

Your friends want you to spend the maximum amount of money, that is, a maximum of the sum of money A[P] + A[Q] + A[R] + A[S]. You put forth a condition that the amount you spend in all four hotels must be strictly increasing, that is, A[P] < A[Q] < A[R] < A[S] to save some money.

Determine the maximum total amount of money that you can spend ensuring that the condition is satisfied, else print 0.

**Note:** A vertex u is called an ancestor of v if it lies on the shortest path between the root and v.

## Input format

- First line: Integer N.
- Next N lines: N integers A1, A2, ..., An where the value of Ai denotes the amount of money charged by a hotel i.
- Next N-1 lines: Two integers a, b denoting a road between the city a and b.

## Output format

Print a single integer denoting the maximum total sum of money that you can spend satisfying the condition, else print 0.
