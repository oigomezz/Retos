# [Shortest Path Revisited][link]

In the country of HackerEarth, there are N cities and M bi - directional roads. We need to transport essential items from City 1 to all other cities. (There exists a path always)

But every road has some positive amount of Toll Charge associated with it say C (it is not same for all roads). We need to find the minimum amount of charge that it required to deliver essential items for each city.

Fortunately, to our rescue we have K special offers, which means while travelling from City 1 to any other city we can select at-most K roads and we will not be charged for using those roads.

Can you now find the minimum charge that we have to pay to deliver essential items for each city.

(Remember we require to provide answers for each destination city separately i.e. we have K offers for every city and not as a whole)

## Input format

- First line contain three integers N M K.
- Next M lines contain three integers U V W, denoting a road between city U and city v with Toll Charge W.

## Output format

Print N space separated integers , denoting the minimum charge we require to pay for each city , where first integer represent cost for City 1, second for City 2 and so on.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/shortest-path-revisited-9e1091ea/
