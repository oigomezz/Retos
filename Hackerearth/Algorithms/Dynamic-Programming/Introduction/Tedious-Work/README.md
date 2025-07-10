# [Tedious Work][link]

John has a very long and tedious project in his current semester, in which he has to write n documents, numbered from 1 to n. The i-th document takes A(i) amount of time to complete. He needs to complete the document in the order of their numbers and he cannot skip any document. In other words, he has to complete 1st document, then 2nd, then 3rd and so on.

He doesn't like to write documents, so he decided to copy documents from the internet. It takes him C(i) amount of time to look for the i-th document online. If he searches for the i-th document, then search result gives him next k documents starting from the i-th document. He can copy these documents to complete the project. After getting k documents (starting from i-th document) he can directly jump to (i+j)th document where 1 ≤ j ≤ k-1 by copying all the documents from index i to (i+j-1) from the search result. It is not necessary for John to copy all k documents. As John hates to write these documents, he wants to spend minimum time doing this project. Help him to determine the minimum time it takes to complete the project. Copy-paste does not take any time.

## Input format

- In the first line, you are given two integers, n (number of documents) and k (maximum continuous documents that John can copy).
- In the second line, you are given an array A with n integers, A(i), where 1 ≤ i ≤ n, represents the time to write the i-th document.
- In the third line, you are given an array C with n integers, C(i), where 1 ≤ i ≤ n, represents the time it takes to look for i-th document online.

## Output format

Print the single Integer, which is the minimum required time to complete the project.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/tedious-work-5593db30/
