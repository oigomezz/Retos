function drawClock(time) {
  const obj = {
    0: [
      ["*", "*", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", "*", "*"],
    ],
    1: [
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
    ],
    2: [
      ["*", "*", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      ["*", "*", "*"],
      ["*", " ", " "],
      ["*", " ", " "],
      ["*", "*", "*"],
    ],
    3: [
      ["*", "*", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      ["*", "*", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      ["*", "*", "*"],
    ],
    4: [
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", "*", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
    ],
    5: [
      ["*", "*", "*"],
      ["*", " ", " "],
      ["*", " ", " "],
      ["*", "*", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      ["*", "*", "*"],
    ],
    6: [
      ["*", "*", "*"],
      ["*", " ", " "],
      ["*", " ", " "],
      ["*", "*", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", "*", "*"],
    ],
    7: [
      ["*", "*", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
    ],
    8: [
      ["*", "*", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", "*", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", "*", "*"],
    ],
    9: [
      ["*", "*", "*"],
      ["*", " ", "*"],
      ["*", " ", "*"],
      ["*", "*", "*"],
      [" ", " ", "*"],
      [" ", " ", "*"],
      ["*", "*", "*"],
    ],
    ":": [
      [" "], 
      [" "], 
      ["*"], 
      [" "], 
      ["*"], 
      [" "],
      [" "]
    ],
    "-": [
      [" "], 
      [" "], 
      [" "], 
      [" "], 
      [" "], 
      [" "], 
      [" "]
    ],
  };
  
  const arr = [[], [], [], [], [], [], []];
  for (const d of time.split("").join("-").split("")) {
    const [r0, r1, r2, r3, r4, r5, r6] = obj[d];
    arr[0].push(...r0);
    arr[1].push(...r1);
    arr[2].push(...r2);
    arr[3].push(...r3);
    arr[4].push(...r4);
    arr[5].push(...r5);
    arr[6].push(...r6);
  }
  return arr;
}