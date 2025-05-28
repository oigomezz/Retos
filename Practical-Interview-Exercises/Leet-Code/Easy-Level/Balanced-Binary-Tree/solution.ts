import { TreeNode } from "../../../tree-node";

function isBalanced(root: TreeNode | null): boolean {
  function check(node: TreeNode | null): number {
    if (node === null) return 0;

    const left = check(node.left);
    if (left === -1) return -1;

    const right = check(node.right);
    if (right === -1) return -1;

    if (Math.abs(left - right) > 1) return -1;

    return Math.max(left, right) + 1;
  }
  return check(root) !== -1;
}
