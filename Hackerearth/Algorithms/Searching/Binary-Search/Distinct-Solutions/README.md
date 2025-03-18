# [Distinct solutions][link]

Bob and Alice decided that problem X needs at least N distinct solutions to be written. It does not matter how many solutions each of them will write, they need to write at least N solutions in total.

Bob needs t1 units of time to write a solution, and Alice needs t2 units of time. They start to work simultaneously at time 0. For example, Bob finishes writing his first solution at time t1, his second solution at 2 \* t1, and so on.

Bob and Alice are working using the same algorithm. Each time Bob or Alice finishes writing a solution, he checks on how many solutions have already been written up to the current time moment t. If the number of such solutions is strictly less than N, then he starts writing the next solution. If a member began working on a problem, he does not stop working under any circumstances and he will surely finish it.

Bob and Alice realize that if they act on this algorithm, they will not necessarily write exactly N solutions in total.

Considering that Bob and Alice work non-stop, find how many solutions they wrote in total and the moment when the latest solution was finished.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains three space-separated integers N, t1 and t2.

## Output format

For each test case, print two integers m and f, where m is the number of written solutions and f is the moment when the last solution was finished. Output for each test case should be in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/distinct-solution-c638e2b0/
