# [Pink and Blue][link]

Xenny was a teacher and he had N students. The N children were sitting in a room. Each child was wearing a white T-shirt, with a unique number from the range 1 to N written on it. T-Shirts of pink and blue color were to be distributed among the students by Xenny. This made the students very happy.

Xenny felt that a random distribution of T-Shirts would be very uninteresting. So, he decided to keep an interesting condition:

Every student would get a T-Shirt that is of a different color than his/her friends. That is, if X and Y are friends and X has a Pink T-Shirt, then Y should compulsorily have a Blue T-Shirt, and vice-versa.

Also, Xenny had a belief that Boys should wear blue T-Shirts and Girls should wear pink T-Shirts. If a boy was given a pink T-Shirt or a girl was given a Blue T-Shirt, he called it an inversion.

So, Xenny wanted to distribute T-Shirts in the above-mentioned interesting manner and also wanted to minimize "inversions". Help him solve the task.

**Note:** There are no disjoint groups of friends in the room. That is, 2 distinct groups with finite number of students do not exist, but exactly 1 group of students exists in the given situation.

## Input format

- First line contains 2 space-separated integers - N and M - number of students and number of friendships present respectively.
- Second line consists of N space-separated characters, where ith character denotes the gender of the ith student. B: Boy, G: Girl.
- M lines follow. Each line consists of 2 space-separated integers, u and v, showing that u is a friend of v and vice-versa.

## Output format

If Xenny could distribute the T-Shirts in the desired way, print the minimum number of inversions required. Else, print "Not possible".

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/pink-and-blue/
