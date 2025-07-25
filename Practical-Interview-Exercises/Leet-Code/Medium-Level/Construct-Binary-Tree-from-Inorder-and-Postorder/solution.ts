import { TreeNode } from "../../../utils/tree-node";

function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
  const inorderValToIdxMap: Record<number, number> = {};
  inorder.forEach((v, i) => (inorderValToIdxMap[v] = i));
  let postOrderRootIdx = postorder.length - 1; //Root idx in postOrder Arr
  //Start end of Inorder traversa (Inclusive),for splitting the arr without changing
  function build(start: number, end: number): TreeNode | null {
    if (start > end) return null;
    const val = postorder[postOrderRootIdx--];
    const InorderRootIdx = inorderValToIdxMap[val];
    const node = new TreeNode(val);
    node.right = build(InorderRootIdx + 1, end);
    node.left = build(start, InorderRootIdx - 1);
    return node;
  }
  return build(0, postorder.length - 1);
}
