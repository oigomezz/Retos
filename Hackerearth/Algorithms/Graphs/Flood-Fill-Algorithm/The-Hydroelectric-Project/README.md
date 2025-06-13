# [The hydroelectric project][link]

A river flows from north to south. You want to harness the river's waters to generate hydroelectricity to keep up with the increasing power demands of your state.

You want to build a hydroelectric power plant in the bottom-right cell. However, to ensure that construction is efficient, you need to stop the river water from coming into that cell. To facilitate this, you decide to build a dam on the river based on the way it flows. You may only build a dam in any cell that is not a rock.

The river water has a natural current (direction of flow). It starts flowing from the top-left cell, and through any cell, it only flows either to the right or to the bottom.

The natural flow of this river can be modeled using a flow model in the form of a grid.

    ...##
    .#.##
    .....
    ##.#.
    ##...

This is what the symbols in the flow model mean:

- Dot (.) symbols: Represent spaces from where the river can flow
- Hashtag (#) symbols: Represent rocks and the river does not flow through these

Using the flow model, you may build a dam (marked as D) only in three cells as shown below to prevent water from entering the bottom-right cell:

    D..##
    .#.##
    ..D..
    ##.#.
    ##..D

If you build the dam in the center (as shown in the grid below), the flow of river water to the bottom-right cell is stopped:

    ...##
    .#.##
    ..D..
    ##.#.
    ##...

However, if you build the dam in any other cell other than the cell in the center, it will not stop the water from entering the bottom-right cell. For example, if you build the dam as follows, the water will still reach the bottom-right cell because at least one path still exists from the top-left cell to the bottom-right cell.

    ...##
    .#D##
    .....
    ##.#.
    ##...

## Task

To build the dam in cell (i, j), you need to spend cost(i, j) units of money. Your task to build the dam by spending the least amount of money.

Determine the minimum cost required to build exactly one dam based on the given river model such that you can stop the river water from entering the bottom-right cell.

## Function description

Complete the buildDam function provided in the editor. This function takes the following 4 parameters and returns the minimum cost to build a dam;

    N: Represents an integer denoting rows of river model
    M: Represents an integer denoting columns of river model
    flow: Represents a string array describing the river model
    cost: Represents a 2D integer array denoting the cost of building a dam

## Input format

- The first line contains a single integer N denoting the rows in the river model.
- The second line contains a single integer M denoting the number of columns in the river model.
- N lines follow, where each line contains a single string of Dots (.) and hashes(#) – describing the river model.
- The next line contains a 2D grid of order N x M, where the cell (i, j) of this grid will tell you the cost associated with building a dam at cell (i, j)

## Output format

Print a single line containing a single integer representing the minimum cost to build a dam on some valid cell.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/flood-fill-algorithm/practice-problems/algorithm/the-hydro-electric-project-2-ae2ed4c4/
