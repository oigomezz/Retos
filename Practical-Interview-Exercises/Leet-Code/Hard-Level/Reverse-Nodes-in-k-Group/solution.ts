import { ListNode } from "../../../list-node";

const reverseKGroup = function (
  head: ListNode | null,
  k: number
): ListNode | null {
  if (!head || k === 1) {
    return head;
  }

  const dummy = new ListNode(0);
  dummy.next = head;

  let prev: ListNode = dummy;
  let curr: ListNode | null = dummy;
  let next: ListNode | null;
  let count = 0;

  while (curr.next) {
    curr = curr.next;
    count++;
  }

  while (count >= k) {
    curr = prev.next;
    if (!curr) break;
    next = curr.next;
    for (let i = 1; i < k; i++) {
      if (!next) break;
      curr.next = next.next;
      next.next = prev.next;
      prev.next = next;
      next = curr.next;
    }
    prev = curr;
    count -= k;
  }

  return dummy.next;
};
