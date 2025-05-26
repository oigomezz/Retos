import { TreeNode } from "../../tree-node";

function preorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];
  const stack: (TreeNode | null)[] = [root];

  while (stack.length > 0) {
    const node = stack.pop();
    if (node) {
      result.push(node.val);
      stack.push(node.right);
      stack.push(node.left);
    }
  }

  return result;
}
