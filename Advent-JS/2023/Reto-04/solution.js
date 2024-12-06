function decode(message) {
  while (message.includes("(")) {
    const startIndex = message.lastIndexOf("(");
    const endIndex = message.indexOf(")", startIndex);

    const start = message.slice(0, startIndex);
    const middle = [...message.slice(startIndex + 1, endIndex)]
      .reverse()
      .join("");
    const end = message.slice(endIndex + 1, message.length);

    message = start + middle + end;
  }
  return message;
}

const a = decode("hola (odnum)");
console.log(a); // hola mundo

const b = decode("(olleh) (dlrow)!");
console.log(b); // hello world!

const c = decode("sa(u(cla)atn)s");
console.log(c); // santaclaus

// Paso a paso:
// 1. Invertimos el anidado -> sa(ualcatn)s
// 2. Invertimos el que queda -> santaclaus
