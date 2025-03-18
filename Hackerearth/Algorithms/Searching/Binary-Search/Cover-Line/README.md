# [Cover Line][link]

Alice was given a number line containing every positive integer, x, where 1 <= x <= n. She was also given m line segments, each having a left endpoint, l (1 <= l <= n), a right endpoint, r (1 <= r <= n), and an integer weight, w.

Her task is to cover all numbers on the given number line using a subset of the line segments, such that the maximum weight among all the line segments in the chosen subset is minimal.

In other words, let S = (l1,r1,w1),(l2,r2,w2),..., (lk,rk,wk), represent a set of k line segments chosen by Alice, max(w1,w2,...,wk) should be minimized.

All numbers 1,2,...,n should be covered by at least one of k the chosen line segments. It is okay for the chosen line segments to overlap.

You program should output the minimized maximum weight in the chosen subset that covers all the numbers on the number line, or -1 if it is not possible to cover the number line.

## Input format

- The first line of the input contains an integer, n - denoting the range of numbers on the number line, [1,n].
- The second line of the input contains an integer, m - denoting the number of line segments.
- The i-th line among the next m lines each contain 3 integers each, li, ri, wi (li <= r1) - denoting the end points, and weight of the i-th line segment. The line segments may overlap.

## Output format

The output should contain one integer, denoting the minimized maximum weight among all the chosen k segments, that completely cover the number line, or -1 if it is not possible to cover the number line.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/cover-points-37bf8bb9/
