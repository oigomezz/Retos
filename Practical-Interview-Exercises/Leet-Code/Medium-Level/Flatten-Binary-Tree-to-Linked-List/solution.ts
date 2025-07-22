import { TreeNode } from "../../../tree-node";

function flatten(root: TreeNode | null): void {
  let current = root;

  while (current) {
    if (current.left) {
      let predecessor = current.left;
      while (predecessor.right) predecessor = predecessor.right;

      predecessor.right = current.right;
      current.right = current.left;
      current.left = null;
    }
    current = current.right;
  }
}
