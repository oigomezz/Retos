import { ListNode } from "../../../list-node";

function partition(head: ListNode | null, x: number): ListNode | null {
  if (!head) {
    return null;
  }

  const l1Root = new ListNode(-1);
  const l2Root = new ListNode(-1);

  let l1 = l1Root;
  let l2 = l2Root;
  let node = head;

  while (node) {
    const next = node.next!;
    if (node.val < x) {
      l1.next = node;
      l1 = l1.next;
      l1.next = null;
    } else {
      l2.next = node;
      l2 = l2.next;
      l2.next = null;
    }

    node = next;
  }

  if (l1.val === -1) return l2Root.next;
  if (l2.val === -1) return l1Root.next;

  l1.next = l2Root.next;

  return l1Root.next;
}
