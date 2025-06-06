# [Quantitative coefficient][link]

It is very important to understand relationship between variables to draw the right conclusion from a statistical analysis. The relationship between variables determines how the right conclusions are reached. Without an understanding of this, you can fall into many pitfalls that accompany statistical analysis and infer wrong results from your data.

Linear programming (LP; also called linear optimization) is a method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships. More formally, linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints.

We are not going to present some LP theory, but let's have a look at combinatorial problem related to this theory. Suppose you have a set of N variables. There are M relationships of some pairs of these variables. More formally, you have M relationships of type ai, bi, ci which means that variables ai and bi are in a relationship with quantitative coefficient ci. Quantitative coefficient of a connected set S of variables is a product of all relationship quantitative coefficients in this set.

Set S of variables is called connected if any two variables in this set are connected. Variables x and y are called connected if at least one of the following conditions is satisfied:

- x and y are put in relationship directly
- there is such a variable z that x and z are connected and y and z are connected too.

You are given a connected set S of N variables and M relationships. Your task is to leave some of these relationships in such a way that S is still connected and its quantitative coefficient is minimal possible.

## Input format

- The first line contains one integer T denoting the number of test cases.
- Each test case starts with a line containing 2 space-separated integer: N and M.
- Each of the following M lines contain description of one relationship: three different space-separated integers: a, b and c. a and b are different and from 1 to N each and denote numbers of vertices that are connected by this edge. c denotes quantitative coefficient of this relationship. It's guaranteed that the given set is initially connected.

## Output format

For each test case output one integer - minimal possible quantitative coefficient. As the the answer can be very big output it modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/quantitative-coefficient/
