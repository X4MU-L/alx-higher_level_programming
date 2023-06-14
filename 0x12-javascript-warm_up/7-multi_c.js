#!/usr/bin/node
// prints x times “C is fun" where x is from line args

const arg = process.argv.slice(2, 3).join();

if (!arg || Number.isNaN(Number(arg))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = Number(parseInt(arg)); i > 0; i--) {
    console.log('C is fun');
  }
}
