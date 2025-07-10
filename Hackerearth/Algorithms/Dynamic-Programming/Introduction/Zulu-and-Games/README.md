# [Zulu and Games][link]

Zulu loves to play games. Once he started playing a very unusual game. The game consists of N levels where each level has two parameters Li & Hi which denotes the lowest and highest energy possible for the i-th level of the game respectively. Now before the start of the game, Zulu has the opportunity to increase his energy which is by default 0. There is a trick called Magic Combo through which Zulu can increase his energy. In Magic Combo, Zulu is allowed to choose several levels as long as their energy levels are non-intersecting. Along with that, after he has finished creating Magic Combo, there should not be any levels left which are not intersecting with the current set of chosen levels and are not picked.

Now, the energy gained after creating a valid Magic Combo is the maximum possible energy amongst all the selected energy levels. As Zulu is very clever, he figured out that he can create many Magic Combos. Can you tell the total possible energy which can be achieved by Zulu after creating all possible Magic Combos? As the total energy value can be very high, return total energy modulus 10⁹ + 7 instead.

Note that two Magic Combos are different if there is at least one level which is different among them. Energy intersection occurs between two levels if they both contain at least one common energy number.

## Input format

- First line contain an integer N denoting the number of levels.
- Second line contains N space separated integers denoting the L array where Li denotes the lowest energy possible for the i-th level.
- Last line contains N space separated integers denoting the H array where Hi denotes the highest energy possible for the i-th level.

## Output format

Output in a single line the maximum energy possible modulus 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/zulu-and-games-0fee9adb/
