function findNaughtyStep(original, modified) {
  // Code here
  let bigger;
  let smaller;
  if(original.length > modified.length){
    bigger = original;
    smaller = modified;
  } else if(original.length < modified.length){
    bigger = modified;
    smaller = original;
  } else {
    return '';
  }

  return bigger.split('').find((char, index) => char !== smaller[index]);
}

const original = "abcd";
const modified = "abcde";
console.log(findNaughtyStep(original, modified)); // 'e'

const original2 = "stepfor";
const modified2 = "stepor";
console.log(findNaughtyStep(original2, modified2)); // 'f'

const original3 = "abcde";
const modified3 = "abcde";
console.log(findNaughtyStep(original3, modified3)); // ''

const original4 = "";
const modified4 = "a";
console.log(findNaughtyStep(original4, modified4)); // 'a'