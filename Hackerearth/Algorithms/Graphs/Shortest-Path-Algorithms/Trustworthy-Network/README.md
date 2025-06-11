# [Trustworthy network][link]

You are a secret agent of S.C.R.E.E.N., who infiltrated the evil organization called Hyena. You have discovered a vital information and want to send it from city s to city e via unidirectional telegraphs.

Unfortunately, you can't trust anyone, so to be sure that the message was delivered and it is correct, you want to receive an acknowledgement message from city e. So if the message was sent through cities s = u1, u2, ..., uk = e, then city e sends an acknowledgement message to u(k-1), then u(k-1) sends an acknowledgement message to u(k-2) and so on, until s receives acknowledgement message.

However, the telegraph lines only work in one direction, thus, the acknowledgement message may be sent back through any other cities. Moreover, for each telegraph line that can send messages from city u to city v there is an information about delivery cost for a single message.

Your task is to find the minimal cost it takes to send message from city s to city e and get an acknowledgement message, or output -1, if it's impossible.

## Input format

- The first line of the input contains four integers n, m, s and e — number of cities, number of telegraph lines and cities, sending and receiving important message, respectively.
- Next m lines describe telegraph lines. Each of this lines contains three integers u, v and t — the city, where the telegraph line starts, the city, where it ends, and amount of money required to deliver the message, respectively. All telegraph lines are unidirectional, there is no telegraph line that connects city with itself, and every telegraph line connects unique ordered pair of cities.

## Output format

The output must contain a single integer — minimum money to be spent, to deliver the message in trustworthy way from city s to city e, or -1, if it's impossible.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/trustworthy-network/
