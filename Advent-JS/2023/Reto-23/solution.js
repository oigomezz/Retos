function organizeChristmasDinner(dishes) {
  const ingredients = {};

  for (const [dish, ...dishIngredients] of dishes) {
    for (const ingredient of dishIngredients) {
      if (ingredients[ingredient]) {
        ingredients[ingredient].push(dish);
      } else {
        ingredients[ingredient] = [dish];
      }
    }
  }

  const result = [];
  for (const ingredient in ingredients) {
    if (ingredients[ingredient].length > 1) {
      result.push([ingredient, ...ingredients[ingredient].sort()]);
    }
  }

  result.sort((a, b) => a[0].localeCompare(b[0]));
  return result;
}

const dishes = [
  ["christmas turkey", "turkey", "sauce", "herbs"],
  ["cake", "flour", "sugar", "egg"],
  ["hot chocolate", "chocolate", "milk", "sugar"],
  ["pizza", "sauce", "tomato", "cheese", "ham"],
];

console.log(organizeChristmasDinner(dishes));

/*

"sauce" está en 2 platos: "christmas turkey" y "pizza".
"sugar" está en 2 platos: "cake" y "hot chocolate".
El resto de ingredientes solo aparecen en un plato, por lo que no los mostramos.

Enseñamos primero "sauce" porque alfabéticamente está antes que "sugar".
Y los platos de cada ingrediente también están ordenados alfabéticamente.

[
  ["sauce", "christmas turkey", "pizza"],
  ["sugar", "cake", "hot chocolate"]
]
*/
