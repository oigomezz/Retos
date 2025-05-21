import { TreeNode } from "../../tree-node";

function minDepth(root: TreeNode | null): number {
  if (!root) return 0;

  const queue: [TreeNode, number][] = [[root, 1]];
  while (queue.length > 0) {
    const item = queue.shift();
    if (!item) break;

    const [node, depth] = item;

    if (!node.left && !node.right) return depth;
    if (node.left) queue.push([node.left, depth + 1]);
    if (node.right) queue.push([node.right, depth + 1]);
  }
  return 0;
}
