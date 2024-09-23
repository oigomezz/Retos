let myArray = [1, 2, 2, 4, 5, 6, 7, 8, 8, 8];
let contador = {}; // Creo un objeto para almacenar la cantidad de veces que se repite cada elemento del array.

myArray.forEach(function (x) {
  // En cada iteración, cuento la cantidad de veces que se repite cada elemento actual del arreglo, y lo almaceno en "contador"
  contador[x] = (contador[x] || 0) + 1;
});

// Hasta aquí ya sabemos la cantidad de veces que se repite cada elemento del arreglo.
// Entonces, ingresemos a los valores de las claves de "contador" y usamos reduce() para
// encontrar el número que se repite más veces.
let masRepetido = Object.keys(contador).reduce(
  (a, b) => (contador[a] > contador[b] ? a : b),
  0
); // aquí retorna el número con mayor cantidad de repeticiones.

console.log("Repetido:", contador[masRepetido]); // obtenemos la cantidad de veces que se repitió el número.
console.log("Numero:", masRepetido);
