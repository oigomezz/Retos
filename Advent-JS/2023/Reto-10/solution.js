function createChristmasTree(ornaments, height) {
  let tree = "";
  let index = 0;

  for (let i = 0; i < height; i++) {
    let row = "";
    tree += " ".repeat(height - i - 1);
    for (let j = 0; j <= i; j++, index++)
      row += ornaments[index % ornaments.length] + " ";

    tree += row.trimEnd() + "\n";
  }
  tree += " ".repeat(height - 1) + "|\n";
  return tree;
}
