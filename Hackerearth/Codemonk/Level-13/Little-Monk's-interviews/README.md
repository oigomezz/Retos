# Little Monk's interviews

Little Monk wants to get a job offer during placement as soon as possible. To increase his chances of getting a job, he wants to give as many interviews at as many different companies as possible. There are N rooms, which are labeled from 1 to N, and in each room a different company is doing its interview process. Between these N rooms, we have M paths which guarantee the fact that the Monk can reach any room from any given room he's in. Every M path takes some T time to travel between two rooms.

Importantly, he wants to maximize his travel time so he can revise his concepts while traveling. Since he's busy preparing for his interviews, help him maximize his travel time so he can prepare for his interviews. Obviously, there will be no cycle allowed in this graph. Since Monk is also enlightened, once he has traveled on a particular path, he takes 0 units of time to travel on it again.

## Input format

- The first line contains an integer TC, which denotes the number of test cases.
- The next line contains two integers, N and M, denoting the number of rooms and number of paths.
- The next M lines contain three integers U, V, and T, where U and V denote the two edges being joined, and T denoting the time taken to travel between U and V.

## Output format

Print the maximum time obtained by Monk to revise his concepts to each test case in a new line.
