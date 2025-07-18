import { TreeNode } from "../../../tree-node";

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  function build(preorder: number[], inorder: number[]): TreeNode | null {
    if (inorder.length) {
      const idx = inorder.indexOf(preorder.shift()!);
      const root = new TreeNode(inorder[idx]);

      root.left = build(preorder, inorder.slice(0, idx));
      root.right = build(preorder, inorder.slice(idx + 1));

      return root;
    }
    return null;
  }

  return build(preorder, inorder);
}
