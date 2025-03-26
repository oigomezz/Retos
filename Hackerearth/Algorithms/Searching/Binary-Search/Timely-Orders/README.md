# [Timely Orders][link]

Today, you have been given a task like ones back end developers face on a daily basis. You need to help in dealing with large amount of requests received in a purchasing application. The application has the following properties:

1. Consumers place large number of orders via this application
2. Each request has a time stamp and an order size associated with it.
3. Each order size is considered in terms of kilo-grams and can be of integer weight only.

Now, the data analytics team needs some information on regular intervals. Based on the requests received in the app, you need to help answer all queries posed by the data-analytics team. So, your task is:

Given 2 types of queries, the first one being of the form 1 X T, indicates an order of weight X is received at time T. The second one is of the form 2 K T indicates that the data analytics team asks you about the summation of weight of the orders received during the last K minutes at time T. The first query can be of the first type only.

For each query, it is guaranteed that they are given in ascending order of time. It means that given q queries and each query having a time T associated with it, T[i] < T[i+1] < T[i+2] < ... < T[q].

## Input format

- The first line contains a single integer q denoting the total number of queries.
- Each of the next q lines contains either of the two types of queries.
  - Each query of type 1 first starts with the number 1 followed by 2 integers X and T.
  - Each query of the second type first starts with the integer 2 and is then followed by 2 integers K and T.

## Output format

For each query of the second type, you need to print the required answer on a new line.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/timely-orders/
