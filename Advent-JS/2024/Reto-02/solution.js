/**
 * @param {string[]} names
 * @returns {string}
 */
function createFrame(names) {
  const maxLength = Math.max(...names.map((name) => name.length));

  const border = "*".repeat(maxLength + 4);

  const framedNames = names.map((name) => {
    const paddedName = name.padEnd(maxLength, " ");

    return `* ${paddedName} *`;
  });

  return [border, ...framedNames, border].join("\n");
}
