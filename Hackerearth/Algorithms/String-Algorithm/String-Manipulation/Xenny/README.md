# [Xenny and Partially Sorted Strings][link]

Xenny had a list of N strings of equal length. He wanted to sort them by the first M characters only. That means, while sorting the list of strings, he only wanted to consider the first M characters of each string.
Help Xenny to find out the Kth string in the list after he sorts them.

**Note:** Xenny wanted to perform stable sorting.

Stable sorting algorithms maintain the relative order of records with equal keys (i.e. values). That is, a sorting algorithm is stable if whenever there are two records R and S with the same key and with R appearing before S in the original list, R will appear before S in the sorted list.

## Input format

- First line contains a single integer - T, which represents the number of testcases.
- T testcases follow. Each testcase is of the following format:
  - First line contains 3 space-separated integers - N, K and M.
    - N is the total number of strings Xenny has.
    - K is the index of the string in the list after sorting, which Xenny has to find.
    - M is the number of characters based on which sorting will be done by Xenny.
  - Then next N lines contain N strings ( each line will contain one string ) .

## Output format

For each testcase, print the Kth string in the sorted list in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/xenny-and-partially-sorted-strings-7/
