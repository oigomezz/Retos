# Little Monk and Williamson

Little Monk is a huge cricket fan, so he decides that he'll meet his five favorite cricketers in this problem-set of heaps. And he'll try to impress them. The first cricketer he wants to impress is: Kane Williamson. He asked Kane to answer some queries in a press interview. Kane is irritated by Little Monk's constant interruption during his interview, so he decides to give Monk a run for his money by asking him the answer to various queries.

Williamson will give a query of the types mentioned below, to the Monk and will expect him to answer those.

- Push X: Insert Williamson's score in an array. - Query type 1.
- Diff: Find out the difference between Willamson's current highest and current lowest score, currently present in the array. And then remove a singular instance of those values from the array. - Query type 2.

  In case, the current lowest and current highest score are same, then only one instance of that score will be removed from the array.

- CountHigh: Find out the number of times Williamson has scored his current highest score, currently present in array. - Query type 3.
- CountLow: Find out the number of times Williamson has scored his current lowest score, currently present in array. - Query type 4.

## Input format

- The first line contains an integer Q, which denotes the number of queries which have to be dealt by The Monk.
- The next Q lines will contain a query like the ones mentioned above.

## Output format

For the query type 2, 3, and 4, print the answer in a new line. If there is no record of any innings, that is, the array of Williamson's score is empty for query type 2, 3 and 4, then print 1.
