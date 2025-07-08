# [The loop problem][link]

Alice and Bob are playing a game to get rid of the boredom during this lockdown. The game consists of N rounds.

Alice challenges Bob in each round of the game by asking for the output of the following loop using the integers A, B, C and D.

    sum = 0;
    for(i=A;i<=B;i++) {
        for(j=C;j<=D;j++) {
            sum = sum + (i^j)
        }
    }
    print(sum)

**Note:** Here ^ stands for Bitwise XOR and other symbols have their usual meanings.

For Bob to win the game, he needs to answer Alice's questions quickly.He needs your help to do this.

## Input format

- The first line contains an integer N denoting the number of rounds in the game.
- The next N lines contain 4 space-separated integers denoting A, B, C and D.

## Output format

Print N lines where each line contains the value of the sum. Since this value can be large, print it modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/loop-problem-db615209/
