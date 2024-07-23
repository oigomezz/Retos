# Missile Bombing

There is N x N field on which missiles are being bombarded. Initially, all the cells in this field have 0 value. There will be M missiles bombarded on this field. ith missile will have power Pi and it will affect all the cells in region with (Ai,Bi) as top-left cornor and (Ci,Di) as bottom-right cornor. Because of missile, value of all the cells in this rectangle will get XOR with Pi.

After all the missiles have been bombarded, you have to find out values in each cell of this field.

## Input format

- First line of input will consists integer N.
- Next line of input will consists of M.
- Next M lines will contain description of missiles. ith line will contain five integers - Pi, Ai, Bi, Ci, Di.

## Output format

You have to print the values in the final field. You have to print N lines, with each line containing the N integers. Integer at ith row and jth column should contain the value present at that position in the field.
