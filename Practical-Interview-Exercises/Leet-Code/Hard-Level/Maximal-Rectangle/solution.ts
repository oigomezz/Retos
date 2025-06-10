function maximalRectangle(matrix: string[][]): number {
    if (matrix.length === 0 || matrix[0].length === 0) return 0;

    const heights = Array(matrix[0].length).fill(0);
    let maxArea = 0;

    for (const row of matrix) {
        for (let i = 0; i < row.length; i++) {
            heights[i] = row[i] === '1' ? heights[i] + 1 : 0;
        }
        maxArea = Math.max(maxArea, largestRectangleArea(heights));
    }

    return maxArea;
};

function largestRectangleArea(heights: number[]): number {
    const stack: number[] = [];
    let maxArea = 0;

    for (let i = 0; i <= heights.length; i++) {
        const currentHeight = i === heights.length ? 0 : heights[i];

        while (stack.length > 0 && currentHeight < heights[stack[stack.length - 1]]) {
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
