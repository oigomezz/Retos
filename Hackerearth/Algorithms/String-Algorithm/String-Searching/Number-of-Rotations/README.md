# [Number of rotations][link]

Bob and his friend James love to play with numbers. Therefore, they both write one number each (X and Y respectively) on stone. Bob wants to impress James by converting his number into special numbers
and Bob knows only three ways that can change his number without touching the stone whare the numbers are written and each way uses K amount of rotations.

The three ways are as follows:

1. Right rotation
2. Left rotation
3. Reverse cloning

If you have a number X = 11 and Y=10.

The binary form of 11 = 1011,10=1010.

The right rotation of 11 = 13 (1011 -> 1101).

The left rotation of 11 = 7 (1011 -> 0111).

Reverse cloning means reverse any bit of the number X. You can perform this operation if and only if the Y has that bit set. You cannot do reverse cloning only on the second and fourth bits.

Print the minimum amount of rotations required to perform this task or print −1 if is is not possible.

**Note:** X and Y are huge numbers. Therefore, they are given in the binary form and the length of the numbers are the same.

## Input format

- The first line contains integer K.
- The next 2 lines contain X and Y in binary form.

## Output format

Print the minimum amount of rotations required to perform this task or print −1 if is is not possible.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/hidden-leaf-village-790b2618/
