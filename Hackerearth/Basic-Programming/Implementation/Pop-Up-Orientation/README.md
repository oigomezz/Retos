# [Pop-Up Orientation][link]

In web application development, it is often required to draw a pop-up window on top of a web page when the user clicks on an icon on the page that brings up the pop-up.
You are given a web page with width x and height y, a pop-up window with width l and height m, and an icon at distance a from the left of the page and distance b from the bottom of the page.
Your program should output the orientation in which the pop-up can be rendered fully, relative to the icon, within the page dimensions. The orientation of pop up should be such that it lies completely within the page.
There are 4 possible orientations: bottom-right, bottom-left, top-right and top-left, in the same order of preference. In other words, you should first attempt to render the pop-up bottom-right, and if that is not possible, try bottom-left, and so on.

**Note:** Icon location and pop-up size are such that the pop-up can always be fully rendered within the page.

## Input format

- First line contains an integer, T, denoting the number of test cases.
- Next T lines contain six space separated integers each, x, y, l, m, a and b.

## Output format

For each test case, print the orientation in which the pop-up can be rendered fully, relative to the icon, within the page dimensions.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/pop-up-orientation-de6cf0ee/
