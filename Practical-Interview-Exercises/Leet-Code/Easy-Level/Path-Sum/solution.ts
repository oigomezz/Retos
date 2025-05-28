import { TreeNode } from "../../../tree-node";

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (!root) return false;

  const stack = [[root, root.val]];
  while (stack.length > 0) {
    const item = stack.pop();
    if (!item) break;

    const [node, currentSum] = item as [TreeNode, number];
    const left = node.left;
    const right = node.right;

    if (!left && !right && currentSum === targetSum) return true;

    if (left) stack.push([left, currentSum + left.val]);
    if (right) stack.push([right, currentSum + right.val]);
  }

  return false;
}
