import { ListNode } from "../../../list-node";

function reverseBetween(
  head: ListNode | null,
  left: number,
  right: number
): ListNode | null {
  if (!head || left === right) return head;

  const dummy = new ListNode(0, head);
  let prev: ListNode = dummy;

  for (let i = 0; i < left - 1; i++) prev = prev.next!;

  let cur: ListNode | null = prev.next;

  for (let i = 0; i < right - left; i++) {
    const temp: ListNode | null = cur!.next;
    cur!.next = temp!.next;
    temp!.next = prev.next;
    prev.next = temp;
  }

  return dummy.next;
}
