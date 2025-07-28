import { TreeNode } from "../../../utils/tree-node";

function sumNumbers(root: TreeNode | null): number {
  if (!root) return 0;

  const dfs = (node: TreeNode | null, currentSum: number): number => {
    if (!node) return 0;

    currentSum = currentSum * 10 + node.val;

    // If it's a leaf node, return the current sum
    if (!node.left && !node.right) return currentSum;

    // Recur for left and right subtrees
    return dfs(node.left, currentSum) + dfs(node.right, currentSum);
  };

  return dfs(root, 0);
}
