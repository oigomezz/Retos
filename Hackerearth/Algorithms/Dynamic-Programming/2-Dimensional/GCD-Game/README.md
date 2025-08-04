# [GCD Game][link]

Life and death, win or lose - both have two sides to each other. And that's what Arjit and Chandu Don are fighting about. They are tired of gang-wars between each other, and thus decide to settle like men in a field, of Mathematics.

But even while going to play the game of Mathematics, they have not given up on their tactics of hurting each other. So, Arjit carries a number of rubber bullets with himself, and Chandu Don carries b number of rubber bullets. Since, Little Chandu is a more dangerous gangster of the two, he decides to give the first chance to Arjit.

The way they’re going to decide who wins the entire land of HEpur is by playing the age-old game of GCD-DCG. The first one to end up with only 1 bullet is going to lose.

This is how the game progresses:

1. If GCD (a, b) is greater than 1, then, the player can:
   - Subtract 1 from opposite player’s bullets.
     **OR**
   - Divide the number of bullets of opposite player by GCD (a, b).
2. If GCD (a, b) is equal to 1, then, the player can:
   - Subtract 1 from the opposite player’s bullets.

**Note:** Player can choose only one move out of two if GCD(A,B)>1 .

The one who ends up with only one bullet loses the battle, and his life, and the land of HEpur.

Determine who is going to rule, once and for all!

## Input format

- First line contains number of test cases T, next T lines contains two numbers A and B taken by Arjit and Chandu Don respectively.

## Output format

Print the name of winner of the game in case of draw print Draw.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/gcd-game-11/
