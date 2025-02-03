# [Mathison and the furthest point][link]

Mathison has taken a course in Computational Geometry. He managed to solve almost all problems from his latest problem sheet. The hardest one was sent to you and is described below.

You are given a C x C grid than currently contains no active points and on which you can perform certain operations.

An operation can be an activation (x,y), in which so you mark the point at coordinates as active if the point was not already marked. Otherwise, you do nothing.

The second type of operation is a query (x,y) (x1,y1) (x2,y2): you have to find the greatest manhattan distance between the point (x,y) and any active point that lies inside the rectangle with the bottom-left corner in (x1,y1) and the top-right one in (x2,y2).

You are given N such operations and you have to execute them all!

## Input format

- The first line of the input file contains one integer, N, representing the number of operations.
- Each of the next N lines will contain either an activation or a query in the following format:
  - 0 x y: mark the point at (x,y) as active.
  - 1 x y x1 y1 x2 y2: find the greatest manhattan distance between (x,y) and any active point from Rectangle( (x1,y1),(x2,y2)).

## Output format

The output file will contain a line for each operation of type 1. If there is no point in the given rectangle, you should print "no point!" (without quotes).

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/mathison-and-the-furthest-point-a502ddf6/
