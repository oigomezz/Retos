import { ListNode } from "../../../list-node";

const mergeKLists = function (lists: (ListNode | null)[]): ListNode | null {
  if (!lists || lists.length === 0) return null;

  while (lists.length > 1) {
    const temp: (ListNode | null)[] = [];
    for (let i = 0; i < lists.length; i += 2) {
      const l1 = lists[i];
      const l2 = i + 1 < lists.length ? lists[i + 1] : null;
      temp.push(mergeLists(l1, l2));
    }
    lists = temp;
  }

  return lists[0];
};

function mergeLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  let node = new ListNode();
  let ans = node;

  while (l1 && l2) {
    if (l1.val > l2.val) {
      node.next = l2;
      l2 = l2.next;
    } else {
      node.next = l1;
      l1 = l1.next;
    }
    node = node.next;
  }

  node.next = l1 || l2;
  return ans.next;
}
