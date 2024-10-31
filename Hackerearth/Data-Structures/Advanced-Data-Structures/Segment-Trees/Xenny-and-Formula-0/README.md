# Xenny and Formula 0

Xenny drove in a popular racing championship called Formula 0. His long-distant friend Mr. Kmcode had made a racing track for him in RSQLand. To entertain the public, he used to keep a drag racing event at the Kmcode Track before every race. The Kmcode Track was circular and there were N grand stands along the track, numbered from 1 to N, separated by 1 angular unit each.

Initially, stand i contained Ai people.

In each drag race, he started from stand number X with initial angular velocity of magnitude w angular units per second. At the end of each second, his car's angular velocity decreased by a magnitude of d angular units per second. His car always came to a halt when its angular velocity reached equal to or below zero.

In each race, Xenny counted the total number of people in stands that he crossed in that race and reported its value modulo 10⁹ + 7, to his team.

Whenever Xenny started his race from a particular stand X, at the end of the race, his team increased the number of passes for his races and hence, Y people were added to stand number X after the race.

Given the data for R races, print the number that Xenny reported to his team in each race.

## Input format

- First line of input contains a single integer R - number of drag races.
- Second line of input contains a single integer N - the number of grand stands.
- Third line contains N space-separated integers - Ai denoting the number of people in i-th stand.
- R lines follow. Each line contains 4 space separated positive integers - X, w, d, Y - the starting stand, the initial angular velocity, the deceleration and the number of people that get added to stand X after each race.

## Output format

Print R lines, i-th line containing the number of people Xenny crosses, modulo 10⁹ + 7, in the i-th race.
