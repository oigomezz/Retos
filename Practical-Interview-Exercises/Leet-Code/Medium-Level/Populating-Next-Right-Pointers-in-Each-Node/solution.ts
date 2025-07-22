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
  if (!root) return null;

  let levelStart: _Node | null = root;
  while (levelStart && levelStart.left) {
    let current: _Node | null = levelStart;
    while (current) {
      if (current.left) current.left.next = current.right;
      if (current.next && current.right) current.right.next = current.next.left;
      current = current.next;
    }
    levelStart = levelStart.left;
  }

  return root;
}
