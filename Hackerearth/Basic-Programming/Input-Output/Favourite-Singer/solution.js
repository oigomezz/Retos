process.stdin.resume();
process.stdin.setEncoding("utf-8");
let stdin_input = "";

process.stdin.on("data", function (input) {
  stdin_input += input;
});

process.stdin.on("end", function () {
  main(stdin_input);
});

function main(input) {
  const [size, array] = input.split("\n");
  const dictionary = {};

  const songs = array.split(" ");

  for (const song of songs) {
    if (dictionary[song]) dictionary[song] += 1;
    else dictionary[song] = 1;
  }

  let counter = 0;
  let key = 0;

  for (const x in dictionary)
    if (counter <= dictionary[x]) counter = dictionary[x];

  for (const x in dictionary) if (counter === dictionary[x]) key += 1;

  process.stdout.write(key);
}
