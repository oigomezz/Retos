# Holiday decorations

Recently, the first model of decoration was assembled from multi-colored glowing light bulbs at the holiday jewelry factory. The prototype of the decoration was assembled as follows:

- First, two light bulbs were taken and connected with a wire.
- Then, a light bulb was taken for N-2 times and it was connected with a wire to one of the previously added to the garland light bulbs.

The result was a decoration of N colored light bulbs. The factory has K bulbs of different colors. When the prototype was ready, it was handed over to the Beauty Department. In this department, it was decided to consider the beauty of jewelry the number of pairs of light bulbs of the same color, connected by a wire.

Employees of the Beauty Department M repaint some of the light bulbs in one of the K colors for some reason known only to them. All they need to produce the perfect jewelry is to quickly determine the beauty of the product, after repainting the next light bulb.

The staff of the beauty department asks you, the best programmer, to write a program that will determine the beauty of jewelry according to the given prototype of jewelry and the sequence of repainting light bulbs.

## Input format

- The first line contains three integers N, M, K denoting the number of bulbs in the product prototype, the number of repaints, and the number of different colors of bulbs available at the factory.
- The second line contains N positive integers Ai denoting the colors of the bulbs in the order of addition to the product.
- The third line contains N - 2 positive integers Pj denoting the number of the light bulb to which the (j+2) light bulb was connected.
- The next M lines contain two integers and denoting the number of the repainted lamp and the color in which it is repainted, respectively. The numbers in the lines are separated by single spaces.

## Output format

Print M lines. The ith line should contain a single integer denoting the number of pairs of light bulbs of the same color, connected by a wire, after execution and repainting.
