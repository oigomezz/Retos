import { TreeNode } from "../../../utils/tree-node";

function generateTrees(n: number): Array<TreeNode | null> {
  if (n === 0) return [];

  const memo = new Map<string, TreeNode[]>();

  const generateTreesHelper = (start: number, end: number): TreeNode[] => {
    if (memo.has(`${start}-${end}`)) return memo.get(`${start}-${end}`)!;

    const trees: TreeNode[] = [];
    if (start > end) {
      trees.push(null);
      return trees;
    }

    for (let rootVal = start; rootVal <= end; rootVal++) {
      const leftTrees = generateTreesHelper(start, rootVal - 1);
      const rightTrees = generateTreesHelper(rootVal + 1, end);

      for (const leftTree of leftTrees) {
        for (const rightTree of rightTrees) {
          const root = new TreeNode(rootVal, leftTree, rightTree);
          trees.push(root);
        }
      }
    }

    memo.set(`${start}-${end}`, trees);
    return trees;
  };

  return generateTreesHelper(1, n);
}
