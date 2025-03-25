# [Round Table Meeting][link]

There are N students in a round table meeting. Each student belongs to a university given in the array Ai, which denotes the university that the i-th student belongs to.

There are Q queries of the form x y, denoting two universities. The answer to each query is the minimum time taken by any one of the student from these universities to meet each other.

## Note

- Exactly 1 student of university x and y have to meet each other.
- In this context, meeting means that the absolute distance between the positions is <= 1.
- Time taken by the student to move from i-th position to (i+1)th or (i-1)th position is exactly 1 second.
- Both the students move together at the same time.
- Both the students move optimally in the correct direction.
- Two students can belong to the same university.
- Round Table means that the nth position and 1st position are adjacent.

## Input format

- The first line of input contains 2 integers N and Q.
- The second line contains N space separated integers denoting A.
- Q lines follow . Each containing 2 integers x and y.

## Output format

The output contains q lines each containing the answer to each query.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/the-graphic-game-59c30775/
