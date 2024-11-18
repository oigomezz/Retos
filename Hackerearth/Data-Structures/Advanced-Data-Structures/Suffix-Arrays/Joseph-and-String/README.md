# Joseph and String

One day, Joseph got a new homework from his teacher. He hates doing homework, especially about the strings. Nick, as his friend, decided to help him. But he didn't know how difficult the problem is!

"Oh my goodness! I can't solve this problem, Joseph !" he said! Of course, Joseph knew that Nick can't solve, so he asked for help on his Facebook page. He still hopes that someone will read this problem and solve for him. So, the problem is as follows:

Given a string S. Also, there are Q queries of following type:

- v l r : you need to find max F(v,i) with i = l to r.

Lets say, t is a concatenation S[l]S[l+1]...S[r], then F(l, r - l + 1) = occur(t,S) \* |t|, where occur(t,S) is the number of occurrences of string t in S.

## Input format

- The first line contains a single integer n — the length of the string S.
- Next line contains a string S consisting of lowercase English letters.
- Next line contains a single integer Q — the number of queries.
- Next Q lines contain three integers each, v,l, and r denoting the query described above.

## Output format

Print the answer for each query.
