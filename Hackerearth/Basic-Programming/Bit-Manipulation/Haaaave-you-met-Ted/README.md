# Haaaave you met Ted!?

The Wingman gains the attention of a prospective partner for their friend, by tapping them on the shoulder, and then stating only the line "Haaaaave you met Ted?" (substituting the name of "Ted", the main protagonist of the show, with the name of the single person), and then walking away, leaving the newly acquainted pair to continue a conversation.

Welcome to the world of 2030, where the process has undergone a technical twist. The people now contact only through systems that use unsigned 31-bit passkeys. The entire arrangement is rather simple, to be honest and the passkeys are just binary representations of unique ids attached to each system.

So, as to establish a connection analogous to the random tap on the shoulder, you must join the two ids. This joining takes time equal to the hamming distance (Read the PS) between the passkeys.

Find the minimum time in which any two systems can get connected. All the ids are stored in form of a set S.

S is characterized by following properties:

- The xor operation is closed in the set, i.e. for any a,b belonging to S, their xor, c=a^b also belongs to S
- None of the numbers are repeated.

## Input format

- First line contains T, the number of test cases
- Each test case contains two lines.
  - The first line has a single integer N.
  - The second line contains N space separated integers representing the set S.

## Output format

A single line for each test case containing the answer as explained in the statement.
