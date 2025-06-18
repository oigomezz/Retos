import { ListNode } from "../../../list-node";

function deleteDuplicates(head: ListNode | null): ListNode | null {
  const dummy = new ListNode(-1);
  dummy.next = head;
  let prev: ListNode = dummy;
  let cur: ListNode | null = head;

  while (cur?.next) {
    if (cur.val === cur.next.val) {
      while (cur.next && cur.val === cur.next.val) cur = cur.next;
      prev.next = cur.next; // Skip all duplicates
    } else prev = prev.next!; // Move to next distinct node
    cur = cur.next;
  }

  return dummy.next;
}
