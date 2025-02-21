/**
 * @typedef {Object} Shoe
 * @property {'I' | 'R'} type
 * @property {number} size
 */

/**
 * @param {Shoe[]} shoes
 * @returns {number[]}
 */
function organizeShoes(shoes) {
  /** @type {Map<number, { I: number; R: number }>} */
  const inventory = new Map();
  /** @type {number[]} */
  const sizes = [];

  for (const shoe of shoes) {
    const { type, size } = shoe;
    if (!inventory.has(size)) inventory.set(size, { I: 0, R: 0 });
    inventory.get(size)[type] += 1;
  }

  for (const [size, counts] of inventory) {
    const numberOfPairs = Math.min(counts.I, counts.R);
    for (let i = 0; i < numberOfPairs; i++) sizes.push(size);
  }

  return sizes;
}

const shoes = [
  { type: "I", size: 38 },
  { type: "R", size: 38 },
  { type: "R", size: 42 },
  { type: "I", size: 41 },
  { type: "I", size: 42 },
];

organizeShoes(shoes);
// [38, 42]

const shoes2 = [
  { type: "I", size: 38 },
  { type: "R", size: 38 },
  { type: "I", size: 38 },
  { type: "I", size: 38 },
  { type: "R", size: 38 },
];
// [38, 38]

const shoes3 = [
  { type: "I", size: 38 },
  { type: "R", size: 36 },
  { type: "R", size: 42 },
  { type: "I", size: 41 },
  { type: "I", size: 43 },
];

organizeShoes(shoes3);
// []
