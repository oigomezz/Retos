# [Matrix and Volume][link]

You are given a large box of length X, width Y and height Z. This box is entirely made up of small cubic boxes of 1 unit volume each i.e. length of cube is 1 unit. Now some cubes were removed to create empty spaces. All the cubes that were not removed stay fixed in their initial position.

Now you are given the information of the new state of the large box i.e. you are given the status of each cube that was used in making the larger box. If the status is 1 then it means that this cubic block was not removed or else if the status is 0 then it corresponds to the fact that this cubic block was removed.

## Important Notes

- Two blocks are adjacent if they share a face.
- A cube with edge size as 1 contains 1 unit cube volume.

Your **task** is to find the volume of air that can stay trapped inside the box in the new state if all the empty space is filed with air. The trapped air means that it should not come outside the box in an infinite amount of time.

## Input format

- First line of input contains T denoting number of test cases.
- First line of each test case contains X,Y,Z, the length, width and height of the box.
- You are also given with the Z sets of X\*Y 2D matrices, each representing a layer of the box.

## Output format

In a single line, return the volume of air that can be trapped.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/trap-gas-e0bcf5ad/
