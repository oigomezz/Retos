function minMovesToStables(reindeer: number[], stables: number[]): number {
  reindeer.sort((a, b) => a - b);
  stables.sort((a, b) => a - b);

  return reindeer.reduce(
    (acc, curr, index) => acc + Math.abs(stables[index] - curr),
    0
  );
}

export default minMovesToStables;
