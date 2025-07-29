# [Rhezo and Special Gift][link]

You are given infinite arrow-bundles, but there are exactly M distinct arrow-bundles. Let us denote them from 1 to M. An arrow-bundle is defined as a set of some number of arrows.

You are also given a target, on which you need to shoot exactly N arrows. In order to do this, you need to pick some arrow-bundles. If you pick some arrow-bundle, you have to use all its arrows and shoot it at the target.

If you can shoot N arrows at the target, you will receive a special gift from Rhezo. For shooting the arrows at target, you have to choose some sequence of arrow-bundles. You are pro at shooting arrows and never miss any shot.

You want to find the number of distinct ways of choosing some sequence of indices of arrow-bundles such that you will receive the gift from Rhezo. Two sequences of indices are distinct if they have different lengths or value at some index is not equal in them.

## Input format

- First line contains 2 space separated integers N and M.
- Next line contains M space separated integers where i-th number denotes the number of arrows in i-th arrow-bundle.

## Output format

Please find the number of distinct ways in which you can get the special gift from Rhezo. As this number can be very large, output your answer modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/rhezo-and-special-gift-2882de10/
