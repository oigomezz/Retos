function countAndSay(n: number): string {
  if (n === 1) return "1";

  let result = "1";
  for (let i = 2; i <= n; i++) {
    let nextResult = "";
    let count = 1;
    for (let j = 1; j < result.length; j++) {
      if (result[j] === result[j - 1]) count++;
      else {
        nextResult += count + result[j - 1];
        count = 1;
      }
    }

    nextResult += count + result[result.length - 1];
    result = nextResult;
  }

  return result;
}
