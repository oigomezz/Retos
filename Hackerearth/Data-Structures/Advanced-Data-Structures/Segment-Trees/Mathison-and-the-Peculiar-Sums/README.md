# Mathison and the peculiar sums

Mathison has bought a new tree from the local market. There was a sale at the market and the tree came with a free set of weights, one weight for each one of its nodes. Mathison is getting bored of just looking at his tree (even though the tree is quite lovely) and starts doing some computations using the weights and the tree's structure.

He starts by choosing a node and getting all the weights on the path from that node to the root (i.e. the node with label 1). He then sorts the weights in increasing order. Next, he sums all the weights that appear in even positions (in the sorted sequence of weights) and then all the weights that appear in odd positions (in the same sorted sequence). The peculiar value of the node is defined to be the product of these two sums.

Mathison performs this calculation for all nodes and wants you to help him make sure that it's correct. Because the numbers are quite large, every peculiar value is computed mod 10⁹ + 7.

## Input format

- The first line of the input file contains one integer N, which represents the number of nodes in Mathison's tree.
- The second line contains N integers representing the weights associated with the nodes. The i-th value is the weight of the node with label i.
- Each of the next N-1 lines contains a pair of integers u and v, representing an edge in Mathison's tree.

## Output format

The output file must contain N lines. The i-th line will contain the peculiar value associated with the i-th node.
