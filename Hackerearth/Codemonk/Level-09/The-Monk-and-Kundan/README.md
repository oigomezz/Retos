# The Monk and Kundan

Kundan being a good friend of Monk, lets the Monk know that he has a following string Initial which consists of the following letters in the mentioned order:

    "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ".

He also has various lists of strings, and now he wants the Monk to compute the Hash value of each list of strings.

Here's the following algorithm used by the Monk to do it.

So, the Hash is the summation of all the character values in the input:

    (currentIndex + (position of the character In the string initial) ).

And then this hash is multiplied by the Number of strings in the list.

Let's assume that the list of strings is: ["aA1", "b"]. So, our answer would be:

    a: 0 + 0 = 0.
    A: 1 + 36 = 37.
    1: 2 + 26 = 28.
    b: 0 + 1 = 1.

So, 2 \* (0 + 1 + 37 + 28 ) = 2 \* (66) = 132.

## Input format

- The first line contains an integer T, denoting the number of test cases.
- For every test case, on a single line, there will be N number of strings all of them separated by a space, denoting all the strings of that particular list of strings.

## Output format

Print the required hash for each of the mentioned list of strings.
