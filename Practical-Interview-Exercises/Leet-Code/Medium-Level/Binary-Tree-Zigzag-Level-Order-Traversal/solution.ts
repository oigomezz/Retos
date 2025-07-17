import { TreeNode } from "../../../tree-node";

function zigzagLevelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];
  const res: number[][] = [];
  const dq: TreeNode[] = [root];
  let reverse = false;

  while (dq.length) {
    const levelSize = dq.length;
    const level: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      if (!reverse) {
        const node = dq.shift()!;
        level.push(node.val);
        if (node.left) dq.push(node.left);
        if (node.right) dq.push(node.right);
      } else {
        const node = dq.pop()!;
        level.push(node.val);
        if (node.right) dq.unshift(node.right);
        if (node.left) dq.unshift(node.left);
      }
    }

    res.push(level);
    reverse = !reverse;
  }

  return res;
}
