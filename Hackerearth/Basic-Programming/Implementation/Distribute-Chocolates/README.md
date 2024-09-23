# Distribute Chocolates

You have c number of chocolates that you want to distribute between your n students. The intelligence level of the students is not the same, therefore, you decide to distribute the chocolates in such a way that a smarter student gets strictly more chocolates than the ones who are less smarter.

The difference between the chocolates received by any two adjacent students must be exactly one. Formally, if the least intelligent student gets k chocolates, then others must get k+1, k+2, k+3, ... . At the same time, your task is to minimize the number of chocolates that are left (if any) after distributing those among students. Determine the minimum number of chocolates left.

It is mandatory to give chocolates to everyone if it is possible to do so. In other words, it is not possible that some students are getting chocolates and others are not.

## Input format

- First line: T denoting the number of test cases
- For each test case (next T lines):
  - First line: Two space-separated integers c and n

## Output format

For each test case, print the minimum number of chocolates left in a new line.
