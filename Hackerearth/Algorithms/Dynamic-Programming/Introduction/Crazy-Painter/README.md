# [Crazy Painter][link]

Abhimanyu simply drew two triangles, as shown in the picture below:

**Drawing Level 1:** He says this, Amazing painting 1.

Then he drew two more triangles, as shown in the picture below:

**Drawing Level 2:** He says this, Amazing painting 2.

Similarly he defined Amazing painting 3, 4, 5, ..., N.

Now he starts finding the points where two lines meet or intersect in the every amazing painting. He names these points as A, B, C, ..., X, Y, Z in Top to Down and Left to Right order and in Cyclic order, i.e., after naming 26th point as Z, he will name 27th point as A, and next points as B, C, D, ...

**Naming:** Every letter A-Z has a self increment cost to it and has initial value equal to CK for 1 <= K <= 26.

Self increment cost means that the cost of any letter is incremented by 1 whenever it comes during naming process again. For example, say you have total 28 points in the painting, and cost of letters A, B is 4, 5 respectively, then when you name the 27th point as A, the cost of letter A will be 5 and similarly when naming 28th point as B, the cost of letter B it will be 6.

This way any painting costs to C, total sum of costs of each letter appeared during naming process. You need to tell Abhimanyu the cost of painting so that he can sell it.

## Input format

- First line of input is an integer T, total number of test cases.
- Each test case consists of two lines.
  - First line of each test case is an integer N, the amazing painting id.
  - Second line contains 26 space separated integers, the initial cost of letters CK.

## Output format

For each test case print the cost of painting in single line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/crazy-painter-4/
