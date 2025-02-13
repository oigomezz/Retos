# [Buy and Sell][link]

A good and robust is always difficult to design, however, its benefits are unlimited and is much better in the long term.

Today, you need to do just the same, i.e. you need to create a system to successfully process the incoming and outgoing stock of a retail outlet.

The outlet stocks and sells N types of items. Each item has a name and a price per unit associated with it. The name of each item on sale is guaranteed to be unique. You shall be given the names and prices for each of the N items.

Now, based on this list of items, You need to process 3 types of queries:

1. X : Given a String X, add one unit of item X to the available stock. It is guaranteed that item X shall be among the list of items the shop trades in.

2. X: If item X exists in the available stock, remove one occurrence of it from the available stock.

3. ? Y: Now, you need to find the summation of available units of each item having price strictly greater than Y.

Initially the stock list is empty. For each query of the 3rd type, you need to print the answer on a new line.

## Input format

- The first line contains a single integers N denoting the number of items the shop trades in.
- Each of the next N lines contains a String X[i] and an integer k[i] where the i-th line denotes that the i-th item has name X[i] and price k[i].
- The next line contains a single integer Q.
- Each of the next Q lines contains either of the 3 types of queries. The first symbol of each query denotes the type of query:
  - A symbol '+' denotes the first type of query.
  - '-' denotes a query of the second type.
  - '?' of the third respectively.

## Output format

For each query of the 3rd type, print the answer on a new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/buy-and-sell/
