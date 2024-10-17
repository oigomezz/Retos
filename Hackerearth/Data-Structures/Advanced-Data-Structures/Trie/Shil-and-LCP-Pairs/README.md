# Shil and LCP Pairs

Shil came across N strings s1, s2, s3,... sN. He wants to find out total number of unordered pairs (i, j) such that LCP(si , sj) = k. You have to do thi for every k in [0, L]. Here L = max(len(si)) and LCP denotes longest common prefix.

## Input format

- First line consists of integer N denoting total number of strings.
- Next N lines consists of strings s1 , s2 , s3 .. sN.

## Output format

Print L+1 integers h0, h1, h2, ..., hL where hi denotes total number of pairs having LCP value i and L = max(len(si)).
