# Smart City

You live in a city that contains N houses. Each house is reachable from every other house through a unique path, which implies that there are N-1 roads in the city. Each of the N-1 road is distinct and has a length denoted by an array L. You want to reach directly from house i to house j (1 <= i,j <= N and i != j) by traversing not more than X units of road length. To reach directly from a house i to house j, you can select exactly one road of length less than or equal to X and destroy that road completely and construct a road between the two houses i and j but the condition is that the every house should be reachable from every other house.

Your task is to solve Q queries (each query is independent from each other ) of the following form:

A B X where (A,B) denotes the pair of the houses that you want to connect. For each query, determine the number of ways in which you can select an ordered pair of houses (G,H) such that the following condidtions hold:

- There should be a road between the houses G and H.
- The length of the road between the houses G and H is less than or equal to X.
- After removing the road between G and H and adding a road between A and B, the houses G and H should still be connected through a path in the city.

## Input format

- First line: Two space-separated integers N and Q.
- Next N-1 lines: Three space-separated integers U, V, and L[i] denoting a bidirectional path from the house U to V and vice versa of length L[i].
- Next Q lines: Three space-separated integers A, B, and X.

## Output format

For each query, print the answer on a separate line.
