const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputLines = [];
rl.on("line", (input) => {
  inputLines.push(input);
});

rl.on("close", () => {
  let currentIndex = 0;
  const testCases = 1;
  const outputResults = [];

  for (let i = 0; i < testCases; i++) {
    const [rows, columns] = inputLines[currentIndex++]
      .trim()
      .split(" ")
      .map(Number);
    const obstaclesCount = +inputLines[currentIndex++];
    const obstacles = inputLines
      .slice(currentIndex, currentIndex + obstaclesCount)
      .map((str) => str.trim().split(" ").map(Number));
    currentIndex += obstaclesCount;
    outputResults[i] = solve(rows, columns, obstacles);
  }

  console.log(outputResults.join("\n"));
});

function solve(rows, columns, obstacles) {
  const obstacleMap = obstacles.reduce((o, [row, column]) => {
    o[hash(row, column)] = 1;
    return o;
  }, {});

  let maxSteps = 0,
    minSteps = 0;

  for (let i = 0; i < rows; i++) {
    let currentStepCount = 0;

    for (let j = 0; j < columns; j++) {
      const positionHash = hash(i, j);

      if (obstacleMap[positionHash]) {
        handleSteps(currentStepCount);
        currentStepCount = 0;
      } else {
        currentStepCount++;
      }
    }

    handleSteps(currentStepCount);
  }

  return [maxSteps, minSteps].join(" ");

  function handleSteps(currentStepCount) {
    if (!currentStepCount) return;

    maxSteps += Math.ceil(currentStepCount / 2);
    minSteps += Math.ceil(currentStepCount / 3);
  }

  function hash(row, column) {
    return row * 1e4 + column;
  }
}
