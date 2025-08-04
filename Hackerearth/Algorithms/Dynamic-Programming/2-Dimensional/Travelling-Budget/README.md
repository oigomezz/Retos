# [Travelling Budget][link]

Recently King Tle4Ever of Time Limit Exceeded gave all the roads of the Kingdom to the private firm named Money Maker. Earlier you were allowed to travel on any road for free. Now, because of the privatization of the roads you have to pay some amount as toll tax to use that road.
As you know the exam season is going on, you need to travel to exam center in another city from your city. As you are not very rich you have limited budget to spend. You want to reach to your exam center as soon as possible within that budget.
There are n cities in Time Limit Exceeded and these cities are connected by m one way roads. Each road i has length li and due to privatization some cost associated with it as ci. Your maximum budget is B.

Your house is located in city 1. You will be given q queries of type x, y where x is the city where you have your exam center and y is the budget in which you want to travel. For each query you have to tell the minimum distance traveled by you to reach your exam center within budget y. If it is not possible to reach within the budget y, print -1 as ans.

## Input format

- First line of input contains a single integer t denoting number of test cases.
- First line of each test case start with 3 integers n, m, B where n is the number of cities, m is number of roads and B is the maximum budget that you have.
- Next m lines contains 4 integers u, v, c, l where u, v denotes that there is one way road from city u to city v, c is the cost associated with that road and l is the length of the road.
- Next line contains a single integer q denoting number of queries.
- Q line follows each having 2 integers x, y where x is the destination city and y is the budget within which you want to reach x.

## Output format

For each query output single line containing minimum distance traveled by you if you can reach that city within that budget else -1.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/travelling-budget/
