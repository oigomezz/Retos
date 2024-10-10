# Population outburst

A new species is trying to rule the planet. This species is creating their own population outburst to dominate other species. It all started with 1 single member of the species. The population increases in treelike fashion abiding by few rules as listed below.

- Single member is able to reproduce by itself.
- A new member is added to the population every minute.
- Every member is associated with integral name.
- Multiple members can share a common name.
- Every member has it's own reproduction capacity, that is maximum number of children it can reproduce.
- A member can start to reproduce only if all members older than it have exhausted their reproduction capacity.
- Level 0 in family tree of this species comprise of single member at the start of multiplication.
- Integral name of single member at the start is 0.
- The population grows level wise, where number of members at level i is dependent on reproduction capacity of members at prior level.

Given the integral name of new member and it's reproduction capacity that is added to the population, you have to find it's parent, level at which it is added and it's ascending age wise rank among siblings.

## Input format

First line of the input contains 2 integers, N, RC0 representing number of minutes we will be examining the population increase and reproduction capacity of member at epoch. Next N line contains 2 integers each, IDi, RCi representing integral name and reproduction capacity of new member born at time i.

## Output format

N lines, each line containing 3 integers, P,L,C representing integral name of the parent, level at which it is added and it's ascending age wise rank among siblings.
