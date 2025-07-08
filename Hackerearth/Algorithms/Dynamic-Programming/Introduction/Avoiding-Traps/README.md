# [Avoiding traps][link]

There is a cave of N cells where each cell has a trap or is safe to land. From a cell i, you can jump to cells i+1 or i+2. Also, if number i is special, then you can also jump from cell i to cell i + A where A = number of primes in [1,i]. A number i can be special if A/i >= r1/r2.

You are given the following:

- Some arbitrary numbers r1 and r2.
- The number of cells N in the cave where each cell contains either '#' or '\*'
- Details of the cave

**Note:** Here, '#' represents an empty cell and '\*' means a trapped cell.

Your task is to determine the minimum number of steps that you have to walk to reach the N-th cell. Initially, you are at cell 1.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains two integers r1 and r2.
- The second line of each test case contains an integer N.
- The third line contains a string of length N representing N cells where the first character of the string represents the first cell, second character represents the second cell, and so on. Each cell is either '#' or '\*'.

## Output format

For each test case, print the minimum number of steps that you have to walk to reach the N-th cell. Print the output in a separate line.

If it is not possible to reach the N-th cell, then print "No way!" without quotes.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/avoid-traps-0b92455e/
