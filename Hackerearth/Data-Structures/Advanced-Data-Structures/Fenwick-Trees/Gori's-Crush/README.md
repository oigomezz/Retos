# [Gori's Crush][link]

Our web developer Gori is having this huge crush on a girl of his batch. But he is very afraid of proposing her. He does not know whether to do it or not. He told this to his best friend Micro, who is an astrologer. Micro came up with an idea to help Gori. He is having a list of N fortune numbers. He asked Gori two numbers, say a & b (a<=b). He also asked two numbers from Gori's crush, say c & d (c<=d) (The numbers a, b, c & d do not necessarily belong to the list). Then he made two lists from fortune numbers. One having fortune numbers which lie between a & b (inclusive) and one having fortune numbers which lie between c & d (inclusive). Then he counted the number of same elements in the two lists and called it the Matching factor, say m. Micro has a special number say k, now if m >= k, then Gori should propose his crush, otherwise not.

But Gori was not satisified with just one result. So they followed above procedure several times for different values of a, b, c & d and Micro also kept updating the list of fortune numbers. This became a hectic task. So they asked you to make a program for it.

## Input format

- The first line consists of three space separated integers N, Q and k.
- Second line consists of N space separated integers, the initial list of fortune numbers.
- The following Q lines contain Q queries. There are two types of queries:
  1. 0 x y, replace xth element in the list by y.
  2. 1 a b c d, print answer for given value of a, b, c, d

## Output format

For each query of type 1, print "Propose" (without quotes) in a new line if for given a, b, c & d value of matching factor, m ≥ k, otherwise print "Do not propose" (without quotes) in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/goris-crush/
