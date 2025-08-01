function canCompleteCircuit(gas: number[], cost: number[]): number {
  let start: number = 0;
  let totalGas: number = 0;
  let currentGas: number = 0;

  for (let i: number = 0; i < gas.length; i++) {
    const fuelGain: number = gas[i] - cost[i];
    totalGas += fuelGain;
    currentGas += fuelGain;

    if (currentGas < 0) {
      currentGas = 0;
      start = i + 1;
    }
  }

  return totalGas < 0 ? -1 : start;
}
