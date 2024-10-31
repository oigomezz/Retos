# Help the Avengers

With the help of the tessaract, the Chitauri army is ready to attack planet Earth. It's finally time when the Avengers must get together to save the planet. Captain Fury, along with the beautiful Agent Maria Hill is trying to work out a plan. He is well aware that Loki, the leader of the enemies has identified certain prime spots to attack. Each spot on the planet is identified by a specific number. A prime spot is one that is represented by a prime number. Now, the Captain's intelligence team has provided him with a list of N locations A[1...N]. From time to time, the team also replaces one location in the list with another one. Every now and then, Captain Fury asks Maria to report the number of prime locations between positions X & Y (inclusive) in the list so that he could position the Avengers at those locations. Now the beautiful lady is tired. Help her.

## Input format

- The first line consists of an integer T, the number of test cases. Then the description of T test cases follow. The first line of each test case consists of an integer N, the number of locations in the list given to Doctor Fury. The next line contains N space separated integers. The next line contains Q, the total number of times either the list is changed or the Captain asks Maria his query. Then Q lines follow, each of the line having one of the following format

1. C X Y - where C is UpperCase alphabet 'C' representing a change in the list, X represents the list index where the change is to be made, Y represents the new location that is added to the above index e.g. C 4 123.

2. A X Y - where A is Uppercase alphabet 'A' representing asking prime spots between indexes X and Y (inclusive) in the list e.g. A 1 12.

## Output format

For each of the query for asking number of prime spots, output a single integer, the answer to Captain Fury's question.
