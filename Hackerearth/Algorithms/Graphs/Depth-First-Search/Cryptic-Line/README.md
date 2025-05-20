# [Cryptic Line][link]

You are given a historical family tree of the noble kingdom, represented as a tree structure. The tree contains information about generations of ancestors and descendants. Your goal is to answer a series of queries in a way that helps people establish their ancestral connections.For each query, you will receive two names, let's call them Person X and Person Y. Person 1 is the root of the family tree. Your task is to determine whether Person X is an ancestor of Person Y or not. If Person X is indeed an ancestor of Person Y, you should respond with YES otherwise, you should reply with NO.Think of yourself as the custodian of this invaluable historical record, helping the kingdom's residents trace their noble lineage. Can you provide accurate responses to these queries and unveil the ancestral ties that bind the kingdom's inhabitants together?

## Input format

- The first line contains an integer N, representing the number of nodes in the family tree.
- The second line contains an integer Q, representing the number of queries.
- The following N-1 lines each contain two space-separated integers U and V indicating an ancestral connection between nodes U and V in the family tree.
- The next Q lines contain two space-separated integers X and Y, representing the individuals for each query.

## Output format

For each query, output either YES if Person X is an ancestor of Person Y, or NO if Person X is not an ancestor of Person Y

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/cryptic-line-92a6bd09/
