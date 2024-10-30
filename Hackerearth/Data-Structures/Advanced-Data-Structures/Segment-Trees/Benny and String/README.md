# Benny and String

Benny loves strings! She also loves to play with string and make different queries on them.

In this problem Benny has a string s of length n consisting of lowercase Latin letters.

Let's define next letter for every lowercase Latin letter. For letters from 'a' to 'y' next letter is next one in Latin alphabet, and for 'z' the next one is 'a'.

Let's call the rotation of letter is when we replace it with the next one.

You have to answer the following queries about the string s:

- ? l r c — where c is lowercase Latin letter, (1 <= l <= r <= n). You have to output the length of the largest sequence consisting of consecutive letters c in s[l,r], where s[l,r] — is the substring of string s starting with s[l] and ending with s[r].
- \+ l r x — you have to rotate every letter in s[l,r] exactly x times, (1 <= l <= r <= n).
- \* i c — set s[i] equal to c, where c is some Latin lowercase letter, (1 <= i <= n).
- \- i x — set s[i] equal to its value before processing the x-th query, (1 <= i <= n), (1 <= x <= j), where j is the index of current query. All queries are indexed starting with 1.

## Input format

- The first line contains two integers n and q denoting the length of the string and the number of queries.
- The next line contains string s.
- The following q lines contains queries.

## Output format

For each query of the first type output an answer as a single integer.
