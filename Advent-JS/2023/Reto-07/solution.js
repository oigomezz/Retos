function drawGift(size, symbol) {
  const endLine = "#\n";
  if (size <= 1) return endLine;

  const pound = "#";
  const lineLength = size * 2 - 1;
  let gift = " ".repeat(lineLength - size) + pound.repeat(size - 1) + endLine;

  const topFace = symbol.repeat(size - 2);
  for (let i = 2; i < lineLength; i++) {
    const calc = lineLength - size - i + 1;
    const prefix = " ".repeat(Math.max(calc, 0)) + pound;
    if (i !== size) {
      const sideFace = pound + symbol.repeat(size - 2 - Math.abs(size - i));
      gift += prefix + topFace + sideFace;
    } else {
      const symbols = symbol.repeat(lineLength - size - 1);
      gift += pound.repeat(size) + symbols;
    }
    gift += endLine;
  }
  gift += pound.repeat(size - 1) + endLine;

  return gift;
}

console.log(drawGift(4, "+"));

/*
   ####
  #++##
 #++#+#
####++#
#++#+#
#++##
####
*/

console.log(drawGift(5, "*"));
/*
    #####
   #***##
  #***#*#
 #***#**#
#####***#
#***#**#
#***#*#
#***##
#####
*/

console.log(drawGift(1, "^"));
/*
#
*/
