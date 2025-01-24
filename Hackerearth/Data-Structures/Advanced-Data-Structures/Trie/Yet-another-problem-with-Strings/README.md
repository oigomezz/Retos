# [Yet another problem with Strings][link]

You are given a 0-indexed array S with N strings, numbered 0 through N-1, and Q queries to handle. All strings in this problem are nonempty and consist of lowercase English letters.

Let's create an integer variable LAST_YES to decipher the input. LAST_YES should be equal to the index of the last query that was of the first type and had an answer "YES". Queries are 0-indexed. LAST_YES is initially equal to zero. Note that LAST_YES can't be changed in the first query because the first query's index is zero.

There are two types of queries.

The first type is of ciphered form "1 t", where t is a string of lowercase English characters. Add LAST_YES to each character in t to get its deciphered value. E.g. the given string cdxyyz with LAST_YES equal to 2 denotes a deciphered string efzaab. You should check whether at least one element of S is a substring of deciphered t. In a single line print "YES" or "NO".

The second type is of ciphered form "2 i alpha", where i and alpha are integers. i (0 ≤ i < |S|) denotes an index in the array S. alpha (0 ≤ alpha < 26) denotes a single lowercase English letter. To decipher a query you should add LAST_YES to i and to alpha. In the other words, you can get a deciphered values using the following C++ and Java code:

    i = (i + LAST_YES) % N;
    alpha = (alpha + LAST_YES) % 26;

After deciphering a query you should add a letter alpha at the end of the i-th string in S.

## Input format

- The first line contains two integers N and Q, denoting the size of the array S and the number of queries, respectively.
- The next N lines describe the array S, one string per line. All strings are nonempty and consist of lowercase English letters.
- The next Q lines contain queries. Each query is of form "1 t" or "2 i alpha".
- For the first type of query, t is a nonempty string of lowercase English letters.
- For the second type, i and alpha are integers, and 0 ≤ i < |S|, 0 ≤ alpha < 26.

## Output format

For each query of the first type print the answer "YES" or "NO" (without the quotes) in a separate line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/b-yet-another-problem-with-strings/
