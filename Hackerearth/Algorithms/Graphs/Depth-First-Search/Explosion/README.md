# [Explosion][link]

There are N cities connected through bidirectional roads and this network forms an tree. The country is very vulnerable to terrorist attacks which is very alarming. The defense sector was notified of a terrorist attack and now they want to protect cities by sending their troops since it has been too late they can't send troops to every city.

The defense sector and terrorists will make a move alternately and the defense sector will go first.

- Defense sector move: They will select a city that has not been chosen yet and send troops there.
- Terrorist move: They will select a city that has not been chosen yet and place a bomb there.

After all the cities have been selected an explosion will take place in which all the cities containing bomb and any city which has road to bomb containing city will be deteriorated. If any city exists which didn't deteriorate, the country is SAFE else UNSAFE.

Note that terrorists wants country to be unsafe while defence sector wants country to be safe so they place troops and bombs optimally.

## Input format

- The first line contains the number of test cases T. For each test case:
  - The first line contains an integer N denoting the number of cities in the country.
  - Next (N-1) lines contain two integers L and R, indicating a bidirectional road between Lth and Rth cities.

## Output format

Print T lines. For each test case:

- If the country is safe, print "SAFE" else "UNSAFE".

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/explosion-2-5f6ef62e/
