type Tree = { value: string; left?: Tree; right?: Tree };

function isTreesSynchronized(tree1?: Tree, tree2?: Tree): [boolean, string] {
  function isMirror(node1: typeof tree1, node2: typeof tree2): boolean {
    if (!node1 && !node2) return true;
    if (!node1 || !node2 || node1.value !== node2.value) return false;

    return (
      isMirror(node1.left, node2.right) && isMirror(node1.right, node2.left)
    );
  }

  if (!tree1) return [false, ""];
  const { value } = tree1;
  const synchronized = isMirror(tree1, tree2);

  return [synchronized, value];
}

export default isTreesSynchronized;
