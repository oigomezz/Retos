import { TreeNode } from "../../../tree-node";
import { ListNode } from "../../../list-node";

function sortedListToBST(head: ListNode | null): TreeNode | null {
  let curr: ListNode | null = head,
    count = 0;
  while (curr) {
    curr = curr.next;
    count++;
  }

  const treeify = (i: number, j: number): TreeNode | null => {
    if (j < i) return null;
    const mid = (i + j) >> 1;
    const node = new TreeNode();
    node.left = treeify(i, mid - 1);
    node.val = curr!.val; // Using non-null assertion since we check j < i
    curr = curr!.next; // Using non-null assertion
    node.right = treeify(mid + 1, j);
    return node;
  };

  curr = head;
  return treeify(1, count);
}
