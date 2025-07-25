import { TreeNode } from "../../../utils/tree-node";

function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result: number[][] = [];
  const queue: (TreeNode | null)[] = [root, null]; // 🌐 Level separator
  let level: number[] = [];

  while (queue.length > 0) {
    const node = queue.shift();

    if (node === null) {
      result.push([...level]); // ✅ Save level
      level = [];
      if (queue.length > 0) queue.push(null); // ➕ Add next level marker
    } else if (node !== undefined) {
      level.push(node.val); // 📥 Add node value
      if (node.left) queue.push(node.left); // ⬅️ Left
      if (node.right) queue.push(node.right); // ➡️ Right
    }
  }

  return result;
}
