# [The Market][link]

There are N items in a market (indexed from 1 to N) each having a particular cost. The danger value of each item is given by the following pseudo code:

    Danger(cost) {
        danger_val = 0
        for ( each i from 1 to cost) {
              if( cost modulo i is 0  ) {
                  increase danger_val by 1
              }
        }
        return danger_val
    }

You are given Q queries which contain a range of items.

You need to find the number of pairs of items that have the same danger value.

## Input format

- First line of the input contains a single integer N
- Second line of the input contains N space-separated integers denoting the prices of the items.
- Third line of the input contains a single integer Q denoting the number of queries
- Each of the next Q lines contain two space-separated integers L and R denoting the range of the items.

## Output format

For each query, print the number of pairs of items that have the same danger value.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/pablos-market-35a291a1/
