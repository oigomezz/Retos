# [Mathison and the Pokémon fights][link]

Mathison has decided to become a Pokémon master. In order to do that he has to gain some experience by fighting in a lot of tournaments, some of which can take quite a lot of time.

Recently, he has signed up for a new one, among other N contestants. Each Pokémon trainer has to use exactly two Pokémons, a primary and a secondary, each having some value. There are s few rules about how the competition should be structured but they are way too complicated to explain here. The rules about fighting are simple and are easily explained below.

A fight can only be carried between Pokémons of equal value (otherwise it would be clear who the winner is). However, this is way too restrictive and the judges have come up with a compromise. A fight can also contain a training period. Basically, the weaker Pokémon spends some time in the PokeGym to become as good as the other one (one second of hard-work is required to gain one hitpoint). The actual fight takes place instantly. To sum up: a fight between two Pokémons of values a and b lasts exactly |a - b| seconds.

A fight between two trainers is actually made from two fights, one between the primary Pokémons and one between the secondary Pokémons, that run at the same time (i.e. they run in parallel). The length of the whole fight is the maximum duration between the two fights.
Note: Pokémons have an awful memory and they forget their training right after their fight ends.

Mathison is trying to find a suitable strategy in order to spend as little time as possible in the gyms. In order to do that, he writes a program that computes how much would it last to fight all the trainers from i to j if a primary Pokémon of value a and a secondary Pokémon of value b are chosen?
The program is complex enough to support updates. From time to time, Mathison finds out that the p-th trainer (i.e. trainer with id p) has changed their pair of Pokémons.

You'd also like a change at becoming a Pokémon master but in order to do that you have to use the same program. Are you able to code it?

## Input format

- The first line of the input file will contain two integers, N and Q, representing the number of trainers and the number of operations.
- Each of the next N lines will contain a pair of integers, value[primary] value[secondary], representing the values of the primary and secondary Pokémons of the corresponding trainer.
- Each of the next Q lines will have one of the following two forms:

  - 0 p value[primary] value[secondary]: the p-th trainer will change their Pokémons to (value[primary], value[secondary])
  - 1 i j value[primary] value[secondary]: How much would it last to fight all trainers with ids from i to j using (value[primary], value[secondary]) as the chosen pair of Pokémons?

## Output format

The output file will contain the answers for the second type of operations. Each answer will be printed on its own line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/mathison-and-the-pokemon-fights-fd8b7c53/
