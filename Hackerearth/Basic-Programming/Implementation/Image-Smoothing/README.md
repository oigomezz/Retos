# [Image Smoothing][link]

Smoothing is used to reduce noise within an image or to produce a less pixelated image. You have been given an image G of resolution N x N. Image will be represented as a 2D grid G of size N x N where Gij will denote intensity of color in a grayscale image of pixel (i,j).

You have been given a filter mask F of size (2 \* M + 1) x (2 \* M + 1). Using this filter mask, you have to perform smoothing operation on the G and output the final image NewG.

## Input format

- First line of input will consists of two integers N and M.
- Next 2 \* M + 1 lines will consists of 2 \* M + 1 integers denoting filter mask F. (M + 1)th integer on (M+2)th line will give the value of F(0,0), first integer on second line will give the value of F(-M,-M) and last integer on (2 \* M + 2)th line will give the value of F(M,M).
- Next N lines will consists of N integers denoting the image G.

## Output format

Output the image NewG obtained by smoothing the image G using filter mask F.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/image-smoothing-3/
