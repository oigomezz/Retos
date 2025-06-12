import { ListNode } from "../../../list-node";

function rotateRight(head: ListNode | null, k: number): ListNode | null {
  if (!head || k === 0) return head;

  let length = 1;
  let tail: ListNode | null = head;
  while (tail.next) {
    tail = tail.next;
    length++;
  }

  k = k % length;
  if (k === 0) return head;

  if (tail) tail.next = head; // form a cycle
  let stepsToNewHead = length - k;
  let newTail: ListNode | null = tail;
  while (stepsToNewHead--) {
    newTail = newTail!.next;
  }

  const newHead: ListNode | null = newTail!.next;
  if (newTail) newTail.next = null;
  return newHead;
}
