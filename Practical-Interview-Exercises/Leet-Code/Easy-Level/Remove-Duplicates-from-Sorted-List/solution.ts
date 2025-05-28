class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val ?? 0;
    this.next = next ?? null;
  }
}

function deleteDuplicates(head: ListNode | null): ListNode | null {
  if (!head) return null;

  let current = head;
  while (current?.next) {
    if (current.val === current.next.val) current.next = current.next.next;
    else current = current.next;
  }
  return head;
}
