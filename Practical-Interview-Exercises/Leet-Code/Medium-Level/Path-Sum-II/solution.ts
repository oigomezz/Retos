import { TreeNode } from "../../../utils/tree-node";

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
  const res: number[][] = [];

  const dfs = (node: TreeNode | null, curSum: number, path: number[]): void => {
    if (!node) return;

    curSum += node.val;
    path.push(node.val);

    if (!node.left && !node.right && curSum === targetSum) res.push([...path]);

    dfs(node.left, curSum, path);
    dfs(node.right, curSum, path);
    path.pop(); // backtrack
  };

  dfs(root, 0, []);
  return res;
}
