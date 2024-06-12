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
  const [number, str] = input.split("\n");
  const res = number * 2;
  process.stdout.write(res.toString());
  process.stdout.write("\n");
  process.stdout.write(str);
}
