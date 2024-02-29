function transformTree(tree) {
  let idx = tree.length - 1;
  tree.forEach(() => {
    tree[idx] = [
      {
        value: tree[idx],
        left: tree[idx * 2 + 1] ?? null,
        right: tree[idx * 2 + 2] ?? null,
      },
      null,
    ][+(tree[idx] === null)];
    idx--;
  });

  return [null, tree[0]][+(tree.length > 0)];
}
