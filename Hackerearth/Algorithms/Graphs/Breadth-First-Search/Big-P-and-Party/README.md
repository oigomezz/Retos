# [Big P and Party][link]

Big P has recently become very famous among girls .

Big P goes to a party and every girl present there wants to dance with him. However, Big P cannot dance with all of them, because there are many of them.

Now if a girl gets to dance with Big P, she considers herself to be " 1-Lucky ". A person that dances with someone who has danced with a person who has danced with Big P considers themselves " 2-Lucky ", and so on.

The Luckiness is defined on the basis of above mentioned rule. ( 1-Lucky -> Luckiness = 1).

## Notes

1. Luckiness of Big P is 0 .
2. No one has negative luckiness.
3. If a person's luckiness cannot be determined from the above rules (he/she has not danced with anyone with finite luckiness), his/her luckiness is INF (infinity).
4. If a person A is not Big P himself, and has danced with someone with luckiness X, and has not danced with anyone with Luckiness smaller than X, then A has luckiness X+1 .

## Input format

- The first line has two numbers A,number of persons in the party and B, number of dancing couples.
- Then B lines follow, each containing two distinct persons, denoting that the two persons have danced. Persons are represented by numbers between 0 and A-1.

Big P is represented by 0.

## Output format

Output A-1 lines , ith line containing the luckiness of ith person. (1<= i <= A-1)

If luckiness cannot be calculated for a person - print "-1"(without the quotes).

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/big-p-and-party-1/
