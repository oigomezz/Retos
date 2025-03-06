# Lovely Circles

In the binary city, small creatures called bino live. These little creatures extremely competitive and always compare themselves with others. also every bino has a fivorite number. We show favorite number of ith bino with fni.

In a competitive environment, ith bino thinks that it's better than the jth bino if and only if the number of 1 in binary representation of (fni | fnj) ^ fni is odd.

In the city of binos A lovely circle is a circle consists of at least two people on which everyone who sits thinks is better than the left bino (next bino in clockwise direction).

Jenny, who is a curiosity girl wants to divide the binos into several groups so that members of each group can form a lovely circle. Help Jenny do it or tell her it can't be done.

## Input format

- The first line contains an integer n denoting the number of binos in the city. (1 <= n <= 5000)
- Next line contains n space-separated integers where the ith integer is fni denotes the favorite number of ith bino. (0 <= fni < 2^(30))

## Output format

If Jenny can't do what she wants, print "NO". Else print "YES" in the first line and then print the grouping in the following format:

In the second line print integer m denoting the number of group. In each of the next m lines, first print the integer k denoting the number of group members. then print k space-separated integers where represent the arrange the members of the group to sit round the circle clockwise.
