function adjustLights(lights) {
  const result = lights.reduce(
    (acc, curr, idx) => {
      const light = idx % 2 ? "🔴" : "🟢";
      curr !== light ? acc[0]++ : acc[1]++;
      return acc;
    },
    [0, 0]
  );
  return Math.min(...result);
}

console.log(adjustLights(["🟢", "🔴", "🟢", "🟢", "🟢"]));
// -> 1 (cambias la cuarta luz a 🔴)

console.log(adjustLights(["🔴", "🔴", "🟢", "🔴", "🟢"]));
// -> 1 (cambia la primera luz a verde)

console.log(adjustLights(["🔴", "🔴", "🟢", "🟢", "🔴"]));
// -> 2 (cambias la segunda luz a 🟢 y la tercera a 🔴)

console.log(adjustLights(["🟢", "🔴", "🟢", "🔴", "🟢"]));
// -> 0 (ya están alternadas)

console.log(adjustLights(["🔴", "🔴", "🔴"]));
// -> 1 (cambias la segunda luz a 🟢)
