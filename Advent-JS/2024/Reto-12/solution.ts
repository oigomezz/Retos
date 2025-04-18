function calculatePrice(ornaments: string): number | undefined {
  const patterns: Record<string, number> = {
    "*": 1,
    "o": 5,
    "^": 10,
    "#": 50,
    "@": 100,
  };

  let prev = patterns[ornaments[ornaments.length - 1]];
  let acc = prev;

  for (let i = ornaments.length - 2; i >= 0; i--) {
    const curr = patterns[ornaments[i]];

    [acc, prev] = curr < prev ? [acc - curr, curr] : [acc + curr, curr];
  }

  return acc || undefined;
}

export default calculatePrice;
