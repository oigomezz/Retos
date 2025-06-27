function grayCode(n: number): number[] {
  const res: number[] = [];
  for (let i = 0; i < 2 ** n; i++) res.push(i ^ Math.floor(i / 2));

  return res;
}
