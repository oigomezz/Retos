# [Reduce the Array][link]

You are given an array of N numbers, and you are asked to minimize the total "OR cost" incurred when reducing the array to a single number. To achieve this, you need to follow these steps:

1. Select any two numbers P and Q from the array. The cost of selecting these two numbers is ((P + Q) + (P | Q) - (P & Q)), where "|" denotes the bitwise OR operator, and "&" denotes the bitwise AND operator.
2. Choose one of the two numbers you selected in the previous step and remove it from the array. Concatenate the remaining numbers.
3. Repeat the above two steps until the array is reduced to a single number.

The "OR cost" is defined as the bitwise OR of all the costs incurred in reducing the array to a single number.

## Input format

- An integer N denoting the size of the array.
- N integers denoting the elements of the array.

## Output format

Print one integer, the minimum OR cost

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/reduce-the-array-2-2a1e3e02/
