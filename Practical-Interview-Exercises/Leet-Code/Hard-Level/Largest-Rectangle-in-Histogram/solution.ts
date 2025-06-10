function largestRectangleArea(heights: number[]): number {
  const stack: number[] = [];
  let maxArea = 0;

  for (let i = 0; i <= heights.length; i++) {
    const currentHeight = i === heights.length ? 0 : heights[i];

    while (
      stack.length > 0 &&
      currentHeight < heights[stack[stack.length - 1]]
    ) {
      const poppedIndex = stack.pop();
      if (poppedIndex !== undefined) {
        const height = heights[poppedIndex];
        const width = stack.length > 0 ? i - stack[stack.length - 1] - 1 : i;
        maxArea = Math.max(maxArea, height * width);
      }
    }
    stack.push(i);
  }

  return maxArea;
}
