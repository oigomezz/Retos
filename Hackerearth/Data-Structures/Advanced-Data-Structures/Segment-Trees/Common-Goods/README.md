# Common Goods

There are N packets of goods each having some number of items in it.The number of items is in the form of an array A (A[i] items of ith type). There are M number of persons in total each having a share in the goods. They have shares in the form of L and R which means that they hold a share of goods [L....R]. Bob wants Q items. He reports the items one by one.
Each time he takes an item you are required to determine how many people have lost all the items from their share.

Note: If Bob wants an item which is unavailable then he will not get it. Here, by "lost all items" we mean that there is not any item left in the share which he holds.

## Input format

- First line contains an integer N(number of goods).
- Then N integers follow representing the number of items of each type of good.
- Then there is an integer M(number of persons) followed by the number 2 .
- Then we have M lines containing 2 integers L and R representing their share.
- Then there is an integer Q followed by Q integers (each integer in a separate line) representing goods which Bob wants.

## Output format

Print Q space separated integers representing the number of people who lost all the items of their share.
