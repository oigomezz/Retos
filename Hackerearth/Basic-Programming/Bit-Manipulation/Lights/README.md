# [Lights][link]

There are N lights, numbered from 1 to N. Initially all of them are switched off. We will consider M days. We represent the state of each day as a string of length N, whose ith character is 1 if the ith light on that day was switched on, and 0 otherwise. Each day one of the following things will happen:

1. L R: All the lights numbered from L to R are flipped, i.e, lights are turned off if they were switched on and vice versa.

2. A B L R: For each light from L to R, count on how many days from Ath day to Bth day, this light was on (Let it be x). Print how many lights (from L to R) are there which were switched on a total odd number of days (i.e, x mod 2 = 1). Also, print the minimum id of light (from L to R), which was switched on a total odd number of days (considering from Ath day to Bth day). State of lights does not change in this type of query.

3. Considering states of all the days till now, which day had the lexicographically largest state (if multiple, print the earliest day). State of lights does not change in this type of query.

## Input format

- First line contains a single integer T, the number of test cases.
- The first line of each test contains two integers, N and M, where N denotes the number of ligths and M denotes the number of days.
- Each of the next M lines starts with an integer K which represents the type of query. If K is 1, it will be followed by two integers L and R. If K is 2, it will be followed by four integers A, B, L and R, where X is the current day number. If K is 3, it will be the only integer in that line.

## Output format

For all the queries that are of type 2 and type 3, print the required answer. In second type of query if no light between L and R was switched on a total odd number of days (between Ath day and Bth day), print "0 0" (without quotes). Also, in third type of query, if there is no change in the state of lights (from 0th day), print "0" (without quotes).

[link]: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/lights-2-c20ca270/
