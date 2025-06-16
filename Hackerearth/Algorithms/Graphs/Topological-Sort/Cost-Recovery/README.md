# [Cost Recovery][link]

Alice is studying the cost of packing chocolates. She has already collected and analyzed some data. Chocolates are packed in boxes that have very weird pricing: it changes as you buy more boxes. The first box one buys always costs b1 burles, the second one costs b2 burles and so on. Some boxes can even have negative price: meaning Alice gets the box for free and additionally gets some burles. Alice has collected the values of b1,b2,..., bn and wrote them down.

Next, she has also computed the sum of all possible distribution and packaging of chocolates. Specifically, for each positive integer k not greater than n: Alice has considered all possible ways to partition k chocolates of different flavors into some boxes, computed the cost of buying those boxes, and added all these costs up to obtain the total cost ak. She has also written down the values of a1,a2,...,an.

Getting a good night's sleep, she finds out to her horror in the morning that Wakandan spies stole her sheet containing values of b1,b2,..., bn. So she asks for your help in recovering the values. But she does not need all the costs to complete her research, only the values of bl,bl+1,..., br.

## Input format

- The first line contains a three space separated integers n,l,r. Here n is the number of values computed by Alice, and (l,r) is the range of values she asks.
- The second line contains n space separated integers: the values of a1,a2,...,an modulo 10⁹ + 7.

## Output format

Print r.l+1 space separated integers: the values of bl,bl+1,..., br modulo 10⁹ + 7.

It is guaranteed that the value of each bi is uniquely determined by the inputs.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/the-last-problem-a090512e/
