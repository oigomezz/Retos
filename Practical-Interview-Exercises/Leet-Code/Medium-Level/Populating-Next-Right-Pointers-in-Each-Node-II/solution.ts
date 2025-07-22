class _Node {
  val: number;
  left: _Node | null;
  right: _Node | null;
  next: _Node | null;

  constructor(
    val?: number,
    left?: _Node | null,
    right?: _Node | null,
    next?: _Node | null
  ) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
    this.next = next === undefined ? null : next;
  }
}

function connect(root: _Node | null): _Node | null {
  if (!root) return root;

  const q: _Node[] = [root];

  while (q.length) {
    const levelSize = q.length;

    for (let i = 0; i < levelSize; i++) {
      const node = q.shift()!;
      if (i < levelSize - 1) node.next = q[0] || null;

      if (node.left) q.push(node.left);
      if (node.right) q.push(node.right);
    }
  }

  return root;
}
