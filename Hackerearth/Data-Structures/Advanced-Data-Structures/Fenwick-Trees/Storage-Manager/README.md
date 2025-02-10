# [Storage manager][link]

Imagine you are the manager of a rental storage facility with N units. The units are represented by a 2D integer array of units where units[i] = [unidId[i], size[i]] denotes that there is a unit with a unit number unitId[i] and size equal to size[i]. Each unitId[i] is guaranteed to be unique.

Your customers have made K requests in a 2D array requests where requests[j] = [preferred[j], minSize[j]]. The answer to the j-th request is the unit number id of a unit such that:

The unit has a size of at minSize[j], and abs(id - preferred[j]) is minimized, where abs(x) is the absolute value of x. If there is no such unit, the answer is -1

Return an array answer of length K where answer[j] contains the answer to the j-th request.

**Note**: If there is a tie in the absolute difference, then use the unit with the smallest such ID.

## Input format

- The first line contains N denoting the number of units.
- Each of the next N lines contains the description of the i-th unit.
- The next line contains K denoting the number of requests.
- Each of the next K lines contains the description of the j-th request.

## Output format

Print an array, representing the result to each query.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/storage-manager-dd942c38/
