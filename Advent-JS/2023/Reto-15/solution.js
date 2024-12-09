function autonomousDrive(store, movements) {
  let row = store.findIndex((_) => _.includes("!"));
  let col = store[row].indexOf("!");
  store[row] = store[row].replace("!", ".");

  for (const move of movements) {
    col += +(store[row][col + 1] === ".") * +(move === "R");
    col -= +(store[row][col - 1] === ".") * +(move === "L");
    row += +(store.at(row + 1)?.at(col) === ".") * +(move === "D");
    row -= +(store.at(row - 1)?.at(col) === ".") * +(move === "U");
  }
  const str = store[row];
  store[row] = str.substring(0, col) + "!" + str.substring(col + 1);
  return store;
}

const store = ["..!....", "...*.*."];

const movements = ["R", "R", "D", "L"];
const result = autonomousDrive(store, movements);
console.log(result);
/*
[
  ".......",
  "...*!*."
]
*/

// El último movimiento es hacia la izquierda, pero no puede moverse porque hay un obstáculo.
