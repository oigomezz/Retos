# [Earthland][link]

There is a mysterious castle in Earthland. In this castle there are 'n' rooms and each room contains "saviour soul" which need to be freed to fight the evil and save earthland. Once the soul is freed it leads to destruction of the room, additionally there is a pathway where you and your friends are standing which is connected to each of the rooms. The castle is so mysterious that if room1 is connected to room2 means you can only go from room1 to room2 and not vice versa. The mystery doesn't end here, starting from a given room, say room(u) it is impossible to reach back to room(u) following any of the paths. Now you need to free all the saviours to save earthland and sacrifice yourself and friends for it. So determine the minimum of your friends who should accompany you for this holy task.

**Note:** You can visit any room from the pathway and after freeing the "saviour soul" you need to run to the next connected room if it exists, otherwise you die.

## Input format

- There are 't' test cases.
- For each test case you will be given 'n' - number of rooms and 'm' - number of connections between rooms.
- Next 'm' lines have two space separated integers say 'u' and 'v' which denotes a way to go from room(u) to room(v). All u,v pairs are distinct where, 1<=u,v<=n.

## Output format

Minimum number of friends who need to sacrifice their life for this noble cause along with you.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/practice-problems/algorithm/earthland/
