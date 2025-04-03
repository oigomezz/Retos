# [One-Sized Game][link]

Ladia and Kushagra are playing the One-Sized Game. The rules of this game are pretty simple.

They have an array consisting of N elements (1-indexed). In each step, one needs to find out the smallest element present in the array. Get the index of that element and subtract that value (index value) from every element of the array. If there is a clash/collision between the smallest element, pick the one that occurs first -- that is the one having smaller index. This process is repeated several times. Whenever an element's value goes below 0 this element gets removed from the array and the array gets re-sized.

During the game's play, if at any point of time, the array is left with only one element, Ladia wins the game otherwise Kushagra wins.

Given an array consisting of N elements, print whether Ladia will win or Kushagra.

## Input format

- The first line contains an integer T denoting the number of test-cases.
- Each test case begins with an integer N that denotes the size of the array.
- This is followed up by N space separated integers.

## Output format

For each test case print whether "Ladia" wins or "Kushagra" (without quotes).

[link]: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/one-sized-game/
