# Binary Blocks

You are given an image, that can be represented with a 2-d n by m grid of pixels. Each pixel of the image is either on or off, denoted by the character ‘0’ or ‘1’, respectively.

You would like to compress this image. You want to choose an integer k > 1 and split the image into k by k blocks. If n and m are not divisible by k, the image to be padded with 0's to the right and/or to the bottom. Each pixel in each individual block must have the same value.

The given image may not be compressible in its current state. Find the minimum number of pixels you need to toggle(padded pixels also can be toggled) in order for the image to be compressible for some k.

More specifically, the steps are to first choose k, then the image is padded with 0s, then, we can toggle the pixels so it is compressible for some k. The image must be compressible in that state.

## Input format

- The first line of input will contain two integers n,m the dimensions of the image.
- The next n lines of input will contain a binary string with exactly m characters, representing the image.

## Output format

Print a single integer, the minimum number of pixels needed to toggle to make the image compressible.
