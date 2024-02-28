/*
  letter => { letter, letterToLowerCase, #, +, :, ., }
  letterToLowerCase => { letterToLowerCase, #, +, :, .,  }
  # => { #, +, :, ., }
  + => { +, :, ., }
  : => { :, .,  }
  . => { .,  }
  ' ' => { }
*/

function checkIsValidCopy(original, copy) {
  if (original.length !== copy.length) return false;
  for (let index = 0; index < original.length; index++) {
    let tests = [];
    const item = original[index];
    if (item === " ") tests = [" "];
    else if (item === ".") tests = [".", " "];
    else if (item === ":") tests = [":",".", " "];
    else if (item === "+") tests = ["+",":",".", " "];
    else if (item === "#") tests = ["#","+",":",".", " "];
    else tests = [item, item.toLowerCase(), "#", "+", ":", ".", " "];
    if (!tests.includes(copy[index])) return false;
  }
  return true;
}

console.log(checkIsValidCopy("Santa Claus is coming", "sa#ta Cl#us i+ comin#")); // true
console.log(checkIsValidCopy("s#nta Cla#s is coming", "p#nt: cla#s #s c+min#")); // false (por la p inicial)
console.log(checkIsValidCopy("Santa Claus", "s#+:. c:. s")); // true
console.log(checkIsValidCopy("s+#:.#c:. s", "s#+:.#c:. s")); // false (hay un # donde no debería)
