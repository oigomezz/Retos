# Monk and Order of Phoenix

Voldemort has a big army, so he has maintained his people in N rows to fight Harry's army. Each row contains the heights of the fighters and is sorted in non-decreasing order from the start to end, except for the first row, which may contain the heights of the fighters in any arbitary order, as it contains all the legendry fighters.

During the war, at any time, Voldemort can remove a fighter from any row, and can also add any new fighter to any row (maintaining the non-decreasing order of heights. except in the first row).

Note:

1. Voldemort will never remove any fighter from an empty row.
2. Voldemort can only remove or add a fighter from/to the end of row.

Now Harry has a special wand which can kill exactly N fighters in one go, but with following conditions:

1. There should be exactly N fighters, and exactly one fighter (which can be anyone in the row) should be chosen from each row.
2. The first fighter can only be chosen from the first row, the second one from second row, and so on. Basically the i-th fighter should be chosen from i-th the row, where i ranges from 1 to N.
3. The order of the heights of the chosen fighters should be strictly increasing.

Now Harry wants to know whether he can kill N fighters using special wand. As Harry is busy in fighting Voldemort, he gave this task to Monk.

## Input format

- The First line consists of a single integer N denoting the number of stacks.
- In each of the next N lines, first integer X denotes the size of the stack, followed by the X space separated integers denoting the heights of the fighters in the stack.
- The next lines consists of single integer Q, denoting the number operations.
- Each of the next Q lines will contain a integer v, which will decide the type of operation.
  1. For v = 1, extra 2 integers k and h will be given , which shows that Voldemort will add one fighter of height h in k-th stack, maintaining the order of the stack, if k is not equal to 1.
  2. For v = 0, 1 more integer k will be given, which shows that Voldemort will remove a fighter from k-th stack.
  3. For v = 2, Monk needs to know whether Harry can use his special wand or not.

## Output format

For each v = 2, print "YES" (without quotes) if Harry can use his special wand or print "NO" (without quotes).
