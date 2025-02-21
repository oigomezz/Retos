/**
 * @param {string[]} box 
 * @returns {boolean}
 */
function inBox(box) {
  return box.slice(1, -1).some(row => /^#.*\*.*#$/.test(row));
}

inBox([
  "###",
  "#*#",
  "###"
]) // ➞ true

inBox([
  "####",
  "#* #",
  "#  #",
  "####"
]) // ➞ true

inBox([
  "#####",
  "#   #",
  "#  #*",
  "#####"
]) // ➞ false

inBox([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) // ➞ false