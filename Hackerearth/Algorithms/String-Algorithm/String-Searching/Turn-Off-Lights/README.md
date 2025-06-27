# [Turn Off Lights][link]

There are n bulbs arranged in a row. The state of the bulbs is represented by a binary string bulbs of length n, the 0 at i-th position in the string represents the bulb is OFF and 1 represents the bulb is ON, where 0 <= i < N. You have to switch OFF all the bulbs by performing following operation atmost k times. The operation is defined as:

- Choose any index i in the string bulb and turn OFF all the lights having indexes i to min(n-1, i+l-1) (inclusive), where l is a pre defined number, greater than zero and fixed for all the operations.

The task is to find the smallest value of l greater than zero, such that you can turn OFF all the bulbs in atmost k operations.

## Input format

- The first line of input contains two space separated integers, n and k, representing the size of string bulb and maximum number of operations you can perform.
- The second line of input contains a binary string, bulbs.

## Output format

The output contains a single integer, the minimum possible value of l greater than zero such that you are able to turn OFF all the bulbs in atmost k operations.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/turn-off-lights-be46dc6c/
