function merge(intervals: number[][]): number[][] {
  if (!intervals.length) return [];

  // Sort intervals by start time
  intervals.sort((a, b) => a[0] - b[0]);

  const merged: number[][] = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const current = intervals[i];
    const lastMerged = merged[merged.length - 1];

    // If the current interval overlaps with the last merged one, merge them
    if (current[0] <= lastMerged[1])
      lastMerged[1] = Math.max(lastMerged[1], current[1]);
    else merged.push(current);
  }

  return merged;
}
