function findBalancedSegment(message) {
  let actual = [0];
  for (let i = 0; i < message.length; i++) {
    let check_balance = message[i];
    let cont = 1;
    for (let j = i + 1; j < message.length; j++) {
      check_balance += message[j];
      if (++cont / check_balance === 2 && cont > actual[0])
        actual = [cont, i, j];
    }
  }
  return actual.slice(1);
}

console.log(findBalancedSegment([1, 1, 0, 1, 1, 0, 1, 1]));
//                                     |________|
// posición del segmento:                [2, 5]
// más largo equilibrado
// de 0s y 1s

console.log(findBalancedSegment([1, 1, 0]));
//                                  |__|
//                                 [1, 2]

console.log(findBalancedSegment([1, 1, 1]));
// no hay segmentos equilibrados: []
