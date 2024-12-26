# [Jumping Tokens][link]

You are given a row of n tokens in a row colored red and blue.

In one move, you can choose to perform a capture. A capture chooses a token, and makes a jump over exactly one other token, and removes a token of the opposite color.

More specifically, given three adjacent tokens we can convert it into the following state with two adjacent tokens:

- RxB -> xR
- BxR -> xB
- RxB -> Bx
- BxR -> Rx

where x is a token of an arbitrary color.

Given the initial row of tokens, return the minimum possible length of the resulting row after a series of captures.

## Input format

- The first line will contain the number of test cases T.
- Each test case can be described with one line.

This line will contain a string consisting of only characters 'R' and 'B' denoting the colors in the row.

## Output format

Output T numbers, the answers to each problem.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/jumping-tokens/
