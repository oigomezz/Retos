# Clothes Arrangement

There is an arrangement of clothes in the form of a stack. There are N clothes with you and each cloth has a color Col[i] associated with it.1st cloth is at the bottom and Nth cloth at the top.

Now you have to answer Q queries, each query can be of 2 types:

- Type-1 query indicated that you place a cloth of color C on top of the stack.
- Type 2 query gives you a color C a number K which means you need to pick the Kth cloth from top having color C.If its not possible print -1.If you find the Kth cloth then you take that cloth out of the stack and put all other clothes back in their original order.For type 2 query if you get a cloth then print the number of clothes you had to pop from the stack before you see your desired cloth.

## Input format

- First line contains an integer N containing the initial number of clothes.
- Next line contains N space separated integers denoting the colors of the ith Cloth.
- Next line contains an integer Q. Each query has a type:
  - For type 1 query you get another integer C.
  - For type 2 query you get 2 integers C and K.

## Output format

Print the answers for the type 2 queries in new line
