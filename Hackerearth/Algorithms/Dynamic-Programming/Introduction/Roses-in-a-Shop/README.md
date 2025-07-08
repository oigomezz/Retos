# [Roses in a shop][link]

There are n roses in a shop. Each rose is assigned an ID. These roses are arranged in order 1,2,3,...,n. Each rose has a smell factor denoted as smell[i] (1 <= i <= n). You want to buy roses from this shop under the condition that you can buy roses in a segment. In other words, you can purchase roses from l to r (1 <= l <= r <= n). You can remove at most one rose from this segment of roses. Thus, the final length of roses is n-1 or n.

Your task is to calculate the maximum possible length of the strictly-increasing contiguous subarray of the smell factors of these roses.

**Note:** A contiguous subarray a with indices from l to r is a[l,...,r] = a[l], a[l+1], ..., a[r-1], a[r]. The subarray a[l,...,r] is strictly increasing if a[l] < a[l+1] < ...< a[r-1] < a[r].

## Input format

- The first line contains a single integer n denoting the number of roses that are available in the shop.
- The second line contains n space-separated integers smell[1], smell[2], ..., smell[n].

## Output format

Print one integer denoting the maximum possible length of the strictly-increasing contiguous subarray of the smell factor after removing at most one element.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/roses-for-valentine-4a795f72/
