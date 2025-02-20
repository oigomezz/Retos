function createFrame(names) {
  const max = names.reduce(
    (acc, name) => (name.length > acc ? name.length : acc),
    0
  );
  const border = "*".repeat(max + 4);
  const body = names
    .map((name) => `* ${name}${" ".repeat(max - name.length)} *`)
    .join("\n");
  return `${border}\n${body}\n${border}`;
}
