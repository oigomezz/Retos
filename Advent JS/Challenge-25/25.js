function travelDistance(map) {
  const pos = {};
  let x = 0;
  let distance = 0;

  for (let line of map.split("\n")) {
    for (let i of ["S", 1, 2, 3, 4, 5, 6, 7, 8, 9]) {
      if (line.includes(i)) pos[i] = [x, line.indexOf(i)];
    }
    x++;
  }

  pos[0] = pos["S"];

  for (let i = 0; i < Object.keys(pos).length - 2; i++) {
    distance += Math.abs(pos[i][0] - pos[i + 1][0]) + Math.abs(pos[i][1] - pos[i + 1][1]);
  }

  return distance;
}

const map = `.....1....
..S.......
..........
....3.....
......2...`;

const result = travelDistance(map);
console.log(result); // -> 12 km
/*
De la S al niño 1: 4 movimientos
Del niño 1 al 2: 5 movimientos
Del niño 2 al 3: 3 movimientos
Total: 12 movimientos
*/

const result2 = travelDistance(`..S.1...`);
console.log(result2); // -> 2
