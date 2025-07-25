import { TreeNode } from "../../../utils/tree-node";

function maxPathSum(root: TreeNode | null): number {
  let res = root ? root.val : 0;

  const dfs = (node: TreeNode | null): number => {
    if (!node) return 0;

    // Recursively compute the maximum sum of the left and right subtree paths.
    const leftSum = Math.max(0, dfs(node.left));
    const rightSum = Math.max(0, dfs(node.right));

    // Update the maximum path sum encountered so far (with split).
    res = Math.max(res, leftSum + rightSum + node.val);

    // Return the maximum sum of the path (without split).
    return Math.max(leftSum, rightSum) + node.val;
  };

  dfs(root);
  return res;
}
