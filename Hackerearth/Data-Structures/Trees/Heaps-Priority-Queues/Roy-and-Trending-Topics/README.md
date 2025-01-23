# [Roy and Trending Topics][link]

Roy is trying to develop a widget that shows Trending Topics (similar to Facebook) on the home page of HackerEarth Academy.

He has gathered a list of N Topics (their IDs) and their popularity score (say z-score) from the database. Now z-score change everyday according to the following rules:

1. When a topic is mentioned in a 'Post', its z-score is increased by 50.
2. A 'Like' on such a Post, increases the z-score by 5.
3. A 'Comment' increases z-score by 10.
4. A 'Share' causes an increment of 20.

Now the Trending Topics are decided according to the change in z-score. One with the highest increment comes on top and list follows.

Roy seeks your help to write an algorithm to find the top 5 Trending Topics.

If change in z-score for any two topics is same, then rank them according to their ID (one with higher ID gets priority). It is guaranteed that IDs will be unique.

## Input format

- First line contains integer N.
- N lines follow:
  - Each contains 6 space separated numbers representing Topic ID, current z-score - Z, Posts - P, Likes - L, Comments - C, Shares - S

## Output format

- Print top 5 Topics each in a new line.
- Each line should contain two space separated integers, Topic ID and new z-score of the topic.

[link]: https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/
