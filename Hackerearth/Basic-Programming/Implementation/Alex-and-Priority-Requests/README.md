# [Alex and Priority Requests][link]

Alex works in a firm that deals with the requests that come with their own Priority Value at different instants of time . Now he has to maintain a list of these requests with their Priority Value and the time at which they come. He updates the list according to the following queries:

- Type 1: Update the Priority Value of the request at time t to p in the list. In case there is no request present at time t in list, set the Priority Value of that request to p at time t in the list.

- Type 2: Remove the request which came at time t, from the list. It is guaranteed that some request has already been come at that time before. Alternatively, there will always be a request at time t currently present in the list.

- Type 3: Print the minimum of Priority Value the request, followed by a space and the maximum Priority Value of the request currently present in the list.

- Type 4: Print the Priority Value of the request, of the highest time present in the list.

**Note:**

1. The time instants given for query 1 may not be in ascending order.
2. There can be more than two time instants with same Priority Value of the request.

## Input format

- First line of the input contains q, the number of queries.
- Then q lines follow.
- Each of the q lines correspond to one of the query mentioned above.
  - Type 1: Integer with value 1, followed by space and two space-separated integers p and t , denoting the Priority Value of the request and time t, respectively.
  - Type 2: Integer with value 2, followed by space and single integer t, denoting the time.
  - Type 3: Integer with value 3.
  - Type 4: Integer with value 4.

## Output format

- For each query of type 3 , output the minimum and maximum Priority Value of the request currently present in the list.
- For each query of type 4, output the Priority Value of the request of highest time, currently present in the list.

**Note:** You can assume that whenever query of type 3,4 occurs, the data is not null i.e some answer exists.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/anil-and-stocks-628d668e/
