function cyberReindeer(road, time) {
  // Code here
  let response = [road];
  let count = 1;
  let newRoad = road.split("");
  let prevStep = '.';

  while (count < time) {
    const santaIndex = newRoad.indexOf("S");
    if (count === 5) {
      for (let index = 0; index < newRoad.length; index++) {
        newRoad[index] = newRoad[index] === "|" ? "*" : newRoad[index];
      }
    }
    if (newRoad[santaIndex + 1] !== "|") {
      newRoad[santaIndex] = prevStep;
      prevStep = newRoad[santaIndex + 1];
      newRoad[santaIndex + 1] = "S";
    }
    response.push(newRoad.join(""));
    count++;
  }
  return response;
}

console.log(cyberReindeer("S..|...|..", 10));

/* -> result:
[
  'S..|...|..', // 0 estado inicial
  '.S.|...|..', // 1 avanza el trineo la carretera
  '..S|...|..', // 2 avanza el trineo la carretera
  '..S|...|..', // 3 el trineo para en la barrera
  '..S|...|..', // 4 el trineo para en la barrera
  '...S...*..', // 5 se abre la barrera, el trineo avanza
  '...*S..*..', // 6 avanza el trineo la carretera
  '...*.S.*..', // 7 avanza el trineo la carretera
  '...*..S*..', // 8 avanza el trineo la carretera
  '...*...S..', // 9 avanza por la barrera abierta
]
*/