# [Write a checker !][link]

Efficient management of a database requires to deal with issues such as Low Latency, Caching and most of all redundancy. Today, you need to perform some testing of a test database provided to you.

Given the database of ABC company, this database contains a table Users. This users table stores for each user 4 pieces of information i.e their Name, Age, Hometown and Address in this order. The size of this table is rather large, and you need to help in resolving some issues.

ABC company is suspicious that this Users table contains many redundant entries. An entry is considered to be redundant if for any 2 separate entries in the table entry i and j, such that i != j, (Namei = Namej) or (Agei = Agej) or (Addressi = Addressj) or (Homertowni = Hometownj).

Now, you need to help ABC company, and write for them a checker, that handles the following :

1. It should be able to detect all pairwise redundant entries.
2. For each pairwise redundant entries i and j, you need to print a new line to output with 2 space separated integers i and j. (The entries are indexed starting from one).

2 entries (i,j) and (x,y) are considered to be pairwise distinct, if i != x or i != y, or j != x or j != y.

## Input format

- The first line contains a single integer N denoting the number of entries in the Users table.
- Each of the next N lines contains 4 space separated tokens mentioned above.

## Output format

On the first line, print a single integer K, i.e the number of redundant entries present in the Users table. On each of the next K lines. print 2 space -separated integers i and j, denoting that entry i and j are pairwise redundant.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/approximate/write-a-checker/
