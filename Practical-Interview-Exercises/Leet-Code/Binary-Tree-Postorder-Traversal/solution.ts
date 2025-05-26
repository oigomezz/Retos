import { TreeNode } from "../../tree-node";

function postorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];
  const stack: (TreeNode | null)[] = [root];

  while (stack.length > 0) {
    const current = stack[stack.length - 1];
    if (current) {
      if (!current.left && !current.right) {
        result.push(current.val);
        stack.pop();
      } else {
        if (current.right) stack.push(current.right);
        stack.push(current.left);
        current.left = current.right = null;
      }
    } else {
      stack.pop();
    }
  }

  return result;
}
