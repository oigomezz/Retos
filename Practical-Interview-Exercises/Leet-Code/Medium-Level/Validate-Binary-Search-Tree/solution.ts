import { TreeNode } from "../../../utils/tree-node";

function isValidBST(root: TreeNode | null): boolean {
  function valid(
    node: TreeNode | null,
    minimum: number,
    maximum: number
  ): boolean {
    if (!node) return true;
    if (!(node.val > minimum && node.val < maximum)) return false;

    return (
      valid(node.left, minimum, node.val) &&
      valid(node.right, node.val, maximum)
    );
  }

  return valid(root, -Infinity, Infinity);
}
