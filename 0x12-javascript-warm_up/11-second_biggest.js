#!/usr/bin/node
// display multiline text

const arg = process.argv.slice(2).map(n => Number(n));

if (arg.length <= 1) {
  console.log(0);
} else {
  let nextSmall = 0; let largest = -Infinity;
  for (let i = 0; i < arg.length; i++) {
    if (largest < arg[i]) {
      nextSmall = largest;
      largest = arg[i];
    } else if (nextSmall < arg[i] && arg[i] !== largest) {
      nextSmall = arg[i];
    }
  }
  console.log(nextSmall);
}
