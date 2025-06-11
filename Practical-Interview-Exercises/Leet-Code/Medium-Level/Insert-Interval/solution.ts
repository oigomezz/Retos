function insert(intervals: number[][], newInterval: number[]): number[][] {
  const merged: number[][] = [];
  let i = 0;

  // Add all intervals that come before the new interval
  while (i < intervals.length && intervals[i][1] < newInterval[0]) {
    merged.push(intervals[i]);
    i++;
  }

  // Merge the new interval with any overlapping intervals
  while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i++;
  }
  merged.push(newInterval);

  // Add all remaining intervals
  while (i < intervals.length) {
    merged.push(intervals[i]);
    i++;
  }

  return merged;
}
