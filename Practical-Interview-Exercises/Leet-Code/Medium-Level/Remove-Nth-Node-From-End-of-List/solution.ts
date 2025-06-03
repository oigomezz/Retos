import { ListNode } from "../../../list-node";

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let dummy = new ListNode(0);
  dummy.next = head;
  let first: ListNode | null = dummy;
  let second: ListNode | null = dummy;

  for (let i = 0; i < n + 1; i++) if (first) first = first.next;

  while (first) {
    first = first.next;
    if (second) second = second.next;
  }

  if (second?.next) second.next = second.next.next;

  return dummy.next;
}
