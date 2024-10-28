# Number of Balloons

You have arranged balloons in a linear order. Every balloon is colored and the i-th balloon's color is represented by Ci. Here, the color of balloons is depicted with numbers.

The number k is not a suitable number, therefore you decide to use it for the less number of times. You do not contain any range of ballons in which a color repeats exactly k times. If the displayed balloons are numbered from b[0],b[1],...,b[n-1], then the range of balloons from l to r is b[l], b[l+1], ..., b[r].

You are provided with some specific ranges and your task is to determine the number of colors that get repeated for exactly k times in each range that is provided.

## Input format

- First line: Three integers n, k, and q. Here, n is the number of balloons, k is the inappropriate number, and q is the number of queries.
- Second line: Contains n integers depicting the color of balloons.
- Each q lines: Contains two integers l and r

## Output format

Print the number of colors that are repeated exactly k times. If the answer to the previous query is ans (answer for the first query is 0), then the range of the answer should be min((l+ans)%n,(r+ans)%n) and max((l+ans)%n,(r+ans)%n).
