# [Aeroplanes Scheduling][link]

There are N aeroplanes scheduled for departure from a runway all arriving at the same destination. All the aeroplanes will depart one by one in the order mentioned which is given by the array S such that the i-th element of the array i.e S[i] gives the constant speed of the i-th aeroplane. Aeroplane will maintain this speed throughout its journey. Also, there are only two elevations available for the aeroplanes currently i.e only two heights are permitted for the aeroplanes and for one particular elevation all the aeroplanes must be in a single straight line. Also an aeroplane i​ will be happy​ only if all the aeroplanes in its elevation and ahead of it are moving at a speed greater than or equal to its speed because only then it wouldn’t have to slow its speed during its course of journey. Schedule the aeroplanes so that the number of happy aeroplanes are maximized. Compute this number. (Consider no collision/overtake during the entire journey and assume the source to destination distance to be very very long)

## Input format

- First line consists of a single integer N denoting the number of aeroplanes.
- Next line consists of N space separated integers with i-th integer denoting S[i] , the speed of i-th aeroplane.

## Output format

Print a single integer denoting the maximum number of happy aeroplanes that can be obtained by some scheduling

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/state-space-reduction/practice-problems/algorithm/aeroplanes-scheduling-7df0c65c/
