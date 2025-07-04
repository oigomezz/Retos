# [Optimal Way][link]

You are provided an array Arr of non-negative integers of size 2\*K. In each round, pick any two integers from the array Arr (number1 and number2) and then eliminate both of them.

The formula for your score in each round is = RoundNumber \* (number1 & number2)

RoundNumber will start from 1 till K, and "number1 & number2" represents bitwise AND of number1 and number2. The total number of rounds is K. The sum of the scores you will receive in each round will represent your final score. Return the maximum possible final score.

## Input format

- The first line contains an integer N, where N denotes the size of the array Arr.
- The second line contains an interger K.

## Output format

Print the maximum possible final score.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/temp-12-d2ff2715/
