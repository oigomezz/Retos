# [Fun Game][link]

A and B are playing a game. In this game, both of them are initially provided with a list of n numbers. (Both have the same list but their own copy).

Now, they both have a different strategy to play the game. A picks the element from start of his list. B picks from the end of his list.

You need to generate the result in form of an output list.

Method to be followed at each step to build the output list is:

1. If the number picked by A is bigger than B then this step's output is 1. B removes the number that was picked from their list.
2. If the number picked by A is smaller than B then this step's output is 2. A removes the number that was picked from their list.
3. If both have the same number then this step's output is 0. Both A and B remove the number that was picked from their list.

This game ends when at least one of them has no more elements to be picked i.e. when the list gets empty.

## Input format

- First line consists of a number n, size of the list provided.
- Next line consists of n numbers separated by space.

## Output format

Output the required output list.

[link]: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/fun-game-91510e9f/
