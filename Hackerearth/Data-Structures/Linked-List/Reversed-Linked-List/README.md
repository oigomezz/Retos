# [Reversed Linked List][link]

You are given a linked list that contains N integers. You have performed the following reverse operation on the list:

- Select all the subparts of the list that contain only even integers. For example, if the list is {1, 2, 8, 9, 12, 16}, then the selected subparts will be {2,8}, {12,16}.
- Reverse the selected subpart such as {8,2} and {16,12}.

Now, you are required to retrieve the original list.

**Note:** You should use the following definition of the linked list for this problem:

    class Node {
      Object data;
      Node next;
    }

## Input format

- First line: N.
- Next line: N space-separated integers that denote elements of the reverse list.

## Output format

Print the N elements of the original list.

[link]: https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/reversed-linked-list-01b722df/
