# [A New Order][link]

Consider a new order of english alphabets (a to z), that we are not aware of. What we have though, dictionary of words, ordered according to the new order.

Our task is to give each alphabet a rank, ordered list of words. The rank of an alphabet is the minimum integer R that can be given to it, such that:

If alphabet Ai has rank Ri and alphabet Aj has Rj, then:

- Rj > Ri if and only if Aj > Ai.
- Rj < Ri if and only if Aj < Ai.

## Points to note

- We only need to find the order of alphabets that are present in the words.
- There might be some cases where a strict ordering of words cannot be inferred completely, given the limited information. In that case, give the least possible Rank to every alphabet.
- It can be assumed that there will be no direct or indirect conflict in different inferences got from the input.

## Input format

- First line consists of integer 'W', the number of words. 1 <= W <= 100.
- Second line onwards, there are 'W' lines, given ordered list of words. The words will be non-empty, and will be of length <= 20 characters. Also all the characters will be lowercase alphabets, a to z.

## Output format

The alphabets, in order of their Rank, for alphabets with the same rank, print them in the order as we know it today.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/a-new-order/
