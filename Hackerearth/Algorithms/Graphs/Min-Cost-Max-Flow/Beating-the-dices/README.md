# [Beating the dices in their own game][link]

A Dice is a really great invention made in the history of the mankind. They try to capture the notion of randomness and one can experience how good they are, by trying to throw a dice such that it lands on a particular integer value written on one of its face. There are many games that revolve around the use of dices and this property of randomness of theirs. Casinos use them heavily to attract customers who try their luck in the hope of winning against the randomness.

However, by the use of modern technology, the star gambler HackerEarthly has made a breakthrough in trying to beat the dices. He has developed a device which can throw a particular face for a dice. But, like most of the devices in the modern world, it needs energy and sometime takes different amount of energy to throw different faces on the same dice.

The Jindal Casino has smelled something fishy by the winning streak of HackerEarthly and has introduced a new tournament to try to stop HackerEarthly. In the tournament, the player will be given N dices given and on each dice, there are Mi faces, with a value written on each of it such that no two faces have the same value. They have done so in the hope of increasing the randomness of a game. They believe that more the number of dices, the more randomness would be there. Now, the tournament consists of Q games, and each game, you will be given a set of N values (K1, .... KN) . The participants win a game if they can throw these exact N values from the N dices given to them. (Note that it is not required that the first value in the game has to be thrown from the first dice, it can be from any, but the value on the top face of each dice will be counted only once.) Note that it is possible that Jindal Casino is cheating and there is no way you can win a game.

Now, HackerEarthly was given the N dices in the beginning with which he will be playing the tournament. He has already computed how much energy he has to use to throw a particular face on a given dice. And he has computed this for all faces for each of the dice given. Since there are multiple games to be played, he is inclined to use minimum energy to win each game. The energy used in a game would be the sum of energies that HackerEarthly requires to throw a particular face on each of his dice. Help him compute the minimum energy value would be required to win each game.

## Input format

- The first line of the input consists of N, the number of dices given to HackerEarthly.
- Then N lines follow, each describing a dice. Each of these N lines start with an integer Mi, the number of faces for that dice, followed by Mi pairs of space separated integers, u and c, where u is the value at a given face for this diceand c is the cost to land that face when the dice is thrown.
- Next line consists of an integer Q, the number of games HackerEarthly is going to play in this tournament.
- Then Q lines follow, each containing N space separated integer values (K1, .... KN) that he is supposed to throw to win this game.

## Output format

Print Q lines, one for each game. Print a single integer which is the minimum energy required by HackerEarthly to win that game. In case, he figures out that it is not possible to win the game, print "-1"

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/practice-problems/algorithm/beating-the-dices-in-their-own-game/
