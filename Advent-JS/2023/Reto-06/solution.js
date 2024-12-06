function maxDistance(movements) {
  const array = movements.split("");
  const moves = {
    ">": 0,
    "<": 0,
    "*": 0,
  };
  for (const char of array) moves[char]++;

  if (moves["<"] > moves[">"]) return moves["<"] + moves["*"] - moves[">"];
  else return moves[">"] + moves["*"] - moves["<"];
}

const movements = ">>*<";
const result = maxDistance(movements);
console.log(result); // -> 2

const movements2 = "<<<>";
const result2 = maxDistance(movements2);
console.log(result2); // -> 2

const movements3 = ">***>";
const result3 = maxDistance(movements3);
console.log(result3); // -> 5

// el nivel que piden esos retos cada vez es más alto y estoy empezando a perder cordura
