import { ListNode } from "../../list-node.ts";

function hasCycle(head: ListNode | null): boolean {
  const visited = new Set<ListNode>();
  let current = head;

  while (current) {
    if (visited.has(current)) return true;
    visited.add(current);
    current = current.next;
  }
  return false;
}
