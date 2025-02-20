function createXmasTree(height, ornament) {
  const treeLines = [];
  for (let i = 0; i < height; i++) {
    const spaces = "_".repeat(height - i - 1);
    const ornaments = ornament.repeat(2 * i + 1);
    treeLines.push(`${spaces}${ornaments}${spaces}`);
  }

  const trunkSpaces = "_".repeat(height - 1);
  const trunk = `${trunkSpaces}#${trunkSpaces}`;

  treeLines.push(trunk);
  treeLines.push(trunk);

  return treeLines.join("\n");
}
