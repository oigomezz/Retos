function organizeGifts(gifts) {
  // Code here
  const breackpoint = /\d+[a-z]/g;
  const elements = gifts.match(breackpoint);
  let pallets = 0;
  let boxes = 0;
  let rest = 0;
  let amount = 0;
  let letter = "";
  let organizeGifts = "";
  for (const gift of elements) {
    amount = parseInt(gift.substring(0, gift.length - 1));
    letter = gift[gift.length - 1];
    pallets = Math.floor(amount / 50);
    boxes = Math.floor(amount / 10) % 5;
    rest = amount % 10;
    if (pallets > 0) organizeGifts += `[${letter}]`.repeat(pallets);
    if (boxes > 0) organizeGifts += `{${letter}}`.repeat(boxes);
    if (rest > 0) organizeGifts += `(${letter.repeat(rest)})`;
  }
  return organizeGifts;
}

const result1 = organizeGifts(`76a11b`);
console.log(result1);
// '[a]{a}{a}(aaaaaa){b}(b)'

/* Explicación:

76a:  76 regalos tipo 'a' se empaquetarían en 7 cajas y sobrarían 6 regalos, 
      resultando en 1 palé [a] (por las primeras 5 cajas), 
      2 cajas sueltas {a}{a} y una bolsa con 6 regalos (aaaaaa)

11b:  11 regalos tipo 'b' se empaquetarían en 1 caja y sobraría 1 regalo, 
      resultando en 1 caja suelta {b} y una bolsa con 1 regalo (b) 

*/
