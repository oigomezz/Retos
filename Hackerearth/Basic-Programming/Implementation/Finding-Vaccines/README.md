# [Finding Vaccines][link]

You are creating a vaccine to fight against a worldwide novel pandemic virus. A vaccine contains a weakened virus that is injected inside people to produce antibodies to let it fight against the virus. The study of interaction among RNA of various viruses is quite necessary for this. An RNA consists of four types of molecules Guanine (G), Adenine (A), Cytosine (C), and Uracil (U).

You are given the structures of RNA for the pandemic virus and several vaccine viruses in the form of strings containing characters G, A, C, and U representing respective molecules. You know that if there is higher interaction between the pandemic virus and vaccine virus, then better the vaccine will be. You also know that the only interaction between any two RNAs is a result of the interaction between their Guanine (G) and Cytosine (C) molecules. Formally, if the strings for RNA structures are s1 and s2, then you must consider the following points:

- One molecule of Guanine (G) of s1 and one molecule of Cytosine (C) of s2 will lead to one unit of interaction.
- One molecule of Guanine (G) of s2 and one molecule of Cytosine (C) of s1 will lead to one unit of interaction.
- Any other pair of molecules do not add to any interactions.

In this way, the total interaction between s1 and s2 is calculated as the sum of individual molecule pair interactions (as discussed above).

You must find the best available vaccine.

## Input format

- The first line contains a single integer n denoting the number of vaccines.
- The second line contains a single integer m denoting the length of the string denoting the RNA structure for the pandemic virus.
- The third line contains a string r denoting the RNA structure for the pandemic virus.
- Next 2n lines contains the following lines where:
  - (2i -1)th line contains a single integer li denoting the length of the string denoting the RNA structure for the ith vaccine virus.
  - (2i)th line contains a string si denoting the RNA structure for the ith vaccine virus

## Output format

Print a single integer k if the kth vaccine is the best, that is, it has the maximum interaction with pandemic virus RNA, where 1 <= k <= n obviously holds.

If there are more than one answers possible (in case of two or more have the maximum interaction value), then print the smallest answer possible.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/find-the-vaccine-a60e06ee/
