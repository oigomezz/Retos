import { ListNode } from "../../../list-node";

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  const dummyHead = new ListNode(0);
  let p = l1,
    q = l2,
    current = dummyHead;
  let carry = 0;

  while (p || q || carry) {
    const x = p ? p.val : 0;
    const y = q ? q.val : 0;
    const sum = x + y + carry;
    carry = Math.floor(sum / 10);
    current.next = new ListNode(sum % 10);
    current = current.next;

    if (p) p = p.next;
    if (q) q = q.next;
  }

  return dummyHead.next;
}
